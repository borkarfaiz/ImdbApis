from flask import Flask
from flask_restful import Resource, Api

from databases import database

from apps.movies.routes import movie_routes
from apps.users.routes import user_routes

from flask_jwt_extended import JWTManager, jwt_required, create_access_token


def create_app():
    app = Flask(__name__)
    # setup with the configuration provided
    app.config.from_object('config.DevelopmentConfig')
    api = Api(app)
    movie_routes(api, "movies")
    user_routes(api, "users")
    jwt = JWTManager(app)
    # setup all our dependencies
    database.init_app(app)

    return app


if __name__ == "__main__":
    create_app().run()
