import re

from bson.objectid import ObjectId
from flask_restful import Resource, request
from databases.helper import get_imdb_db

from flask_jwt_extended import jwt_required
from apps.users.helper import admin_required

from .parser import movies_create_parser, movies_update_parser, movies_delete_parser, \
    movies_search_parser


class Search(Resource):
    @jwt_required()
    # @admin_required()
    def get(self):
        import re
        imdb_db = get_imdb_db()
        request_params = request.args.to_dict()['name']
        regex = re.compile(f".*{request_params}.*", re.IGNORECASE)
        list_of_movies = list(imdb_db.movies.find({'name': regex}).sort('99popularity', -1))
        for movie in list_of_movies:
            movie["id"] = str(movie.pop("_id"))
        return list_of_movies


class Movie(Resource):
    @jwt_required()
    def get(self):
        parser = movies_search_parser()
        parsed_args = parser.parse_args()
        parsed_args = {key: value for key, value in parsed_args.items() if value is not None}
        imdb_score_range = parsed_args.get('imdb_score_range')
        if imdb_score_range:
            from_, to_ = imdb_score_range
            parsed_args.pop("imdb_score_range")
            parsed_args.update({"imdb_score": {"$lte": to_, "$gte": from_}})
        _99popularity_range = parsed_args.get('99popularity_range')
        if _99popularity_range:
            from_, to_ = _99popularity_range
            parsed_args.pop("99popularity_range")
            parsed_args.update({"99popularity": {"$lte": to_, "$gte": from_}})        
        name = parsed_args.get('name')
        if name:
            regex = re.compile(f".*{name}.*", re.IGNORECASE)
            parsed_args.update({'name': regex})
        director = parsed_args.get('director')
        if director:
            regex = re.compile(f".*{director}.*", re.IGNORECASE)
            parsed_args.update({'director': regex})
        genres = parsed_args.get('genres')
        if genres:
            parsed_args.pop('genres')
            parsed_args.update({"genre":{"$all": genres}})
        db = get_imdb_db()
        query = db.movies.find(parsed_args).sort('99popularity', -1)
        # 
        limit, offset = parsed_args.get('limit'), parsed_args.get('offset')
        if limit is not None and offset is not None:
            movies = query.skip(offset).limit(limit)
            parsed_args.pop('limit')
            parsed_args.pop('offset')
        elif limit:
            parsed_args.pop('limit')
            movies = query.limit(limit)
        else:
            movies = query
        list_of_movies = list(movies)
        for movie in list_of_movies:
            movie['id'] = str(movie.pop("_id"))
        return {"result": list_of_movies, "total_count": query.count()}, 200

    @jwt_required()
    @admin_required
    def delete(self):
        parser = movies_delete_parser()
        parsed_args = parser.parse_args()
        id = parsed_args.pop("id")
        db = get_imdb_db()
        deleted = db.movies.find_one_and_delete({"_id": ObjectId(id)})
        if not deleted:
            return "no record found", 404
        deleted['id'] = str(deleted.pop("_id"))
        return deleted, 200

    @jwt_required()
    @admin_required
    def put(self):
        parser = movies_update_parser()
        parsed_args = parser.parse_args()
        id = parsed_args.pop("id")
        parsed_args = {key: value for key, value in parsed_args.items() if value is not None}
        if not parsed_args:
            return 'no values provided', 400
        db = get_imdb_db()
        db.movies.find_one_and_update({"_id": ObjectId(id)}, {"$set": parsed_args})
        updated_data = db.movies.find_one({"_id": ObjectId(id)})
        updated_data["id"] = str(updated_data.pop("_id"))
        return updated_data, 200

    @jwt_required()
    @admin_required
    def post(self):
        parser = movies_create_parser()
        parsed_args = parser.parse_args()
        db = get_imdb_db()
        if db.movies.find_one({'name': parsed_args.get('name'), 'director': parsed_args.get('director')}):
            return "already exist", 409
        id = db.movies.insert_one(parsed_args)
        id = str(id.inserted_id)
        parsed_args.update({"id": id})
        parsed_args.pop('_id')
        return parsed_args, 201
