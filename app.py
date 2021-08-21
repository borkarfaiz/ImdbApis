from flask import Flask
from databases import database
from flask_restful import Resource, Api


from apps.app_1.routes import  initialize_routes

def create_app():
    app = Flask(__name__)
    # setup with the configuration provided
    app.config.from_object('config.DevelopmentConfig')

    api = Api(app)
    initialize_routes(api)

    # setup all our dependencies
    database.init_app(app)

    return app

if __name__ == "__main__":
    create_app().run()