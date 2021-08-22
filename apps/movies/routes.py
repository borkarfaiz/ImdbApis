from .views import Search, Movie
from utils import generate_url


def movie_routes(api, base_url):
    api.add_resource(Search, generate_url([base_url, 'search']))
    api.add_resource(Movie, generate_url([base_url]))