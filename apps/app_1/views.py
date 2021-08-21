from flask import Blueprint, request, url_for, redirect, render_template, flash
from flask_restful import Resource

app1 = Blueprint('app1', __name__, template_folder="templates/app1")


class HelloWorld(Resource):
    def get(self):
        return {'hello': {'h1': 'world'}}


class Samjha(Resource):
    def get(self):
        return {'Samjha': {'hello': {'h1': 'world'}}}
