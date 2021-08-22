from bson.objectid import ObjectId
from flask_restful import Resource, request
import jwt
from databases.helper import get_imdb_db

from flask_jwt_extended import jwt_required
from apps.users.helper import admin_required

from .parser import movies_create_parser, movies_update_parser, movies_delete_parser


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
        return "get"
    
    @jwt_required()
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
