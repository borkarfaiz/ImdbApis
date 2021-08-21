from flask import Blueprint, url_for, redirect, render_template, flash
from flask_restful import Resource, request
from databases.database import db
from databases.helper import get_imdb_db

class HelloWorld(Resource):
    def get(self):
        return {'hello': {'h1': 'world'}}


class Samjha(Resource):
    def get(self):
        return {'Samjha': {'hello': {'h1': 'world'}}}


class Search(Resource):
    def get(self):
        import re
        imdb_db = get_imdb_db()
        request_params = request.args.to_dict()['name']
        regex = re.compile(f".*{request_params}.*", re.IGNORECASE)
        list_of_movies = list(imdb_db.movies.find({'name': regex}, {"_id": 0,}).sort('99popularity', -1))
        return list_of_movies


