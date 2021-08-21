from flask import Flask
# from database import database
from flask_restful import Resource, Api

# blueprint import
from apps.app_1.views import app1
from apps.app_1.routes import  initialize_routes
# from apps.app2.views import app2


def create_app():
    app = Flask(__name__)
    api = Api(app)
    initialize_routes(api)
    # setup with the configuration provided
    # app.config.from_object('config.DevelopmentConfig')
    
    # setup all our dependencies
    # database.init_app(app)
    
    # register blueprint
    # api.add_resource(HelloWorld, '/')
    # app.register_blueprint(app1)
    
    # app.register_blueprint(app2, url_prefix="/app2")
    
    return app

if __name__ == "__main__":
    create_app().run()