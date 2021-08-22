from flask_restful import reqparse
from .validators import validate_name, validate_99popularity, validate_genre, \
    validate_imdb_score, validate_99popularity_range, validate_imdb_score_range, validate_genre_list

def movies_create_parser():
    parser = reqparse.RequestParser()
    parser.add_argument("name", type=validate_name, location="json", required=True)
    parser.add_argument("99popularity", type=validate_99popularity, location="json", required=True)
    parser.add_argument("genre", type=validate_genre, location="json", required=True)
    parser.add_argument("imdb_score", type=validate_imdb_score, location="json", required=True)
    parser.add_argument("director", type=validate_name, location="json", required=True)
    return parser


def movies_update_parser():
    parser = reqparse.RequestParser()
    parser.add_argument("id", type=str, location="json", required=True)
    parser.add_argument("name", type=validate_name, location="json", required=False)
    parser.add_argument("99popularity", type=validate_99popularity, location="json", required=False)
    parser.add_argument("genre", type=validate_genre, location="json", required=False)
    parser.add_argument("imdb_score", type=validate_imdb_score, location="json", required=False)
    parser.add_argument("director", type=validate_name, location="json", required=False)
    return parser
  

def movies_delete_parser():
    parser = reqparse.RequestParser()
    parser.add_argument("id", type=str, location="json", required=True)
    return parser


def movies_search_parser():
    parser = reqparse.RequestParser()
    parser.add_argument("name", type=validate_name, location="args", required=False)
    parser.add_argument("99popularity_range", type=validate_99popularity_range, location="args", required=False)
    parser.add_argument("genres", type=validate_genre_list, location="args", required=False)
    parser.add_argument("imdb_score_range", type=validate_imdb_score_range, location="args", required=False)
    parser.add_argument("director", type=validate_name, location="args", required=False)
    parser.add_argument("limit", type=int, location="args", required=False)
    parser.add_argument("offset", type=int, location="args", required=False)
    return parser