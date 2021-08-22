from .views import HelloWorld, Samjha, Search
from utils import generate_url


def movie_routes(api, base_url):
    api.add_resource(HelloWorld, generate_url([base_url, 'h']))
    api.add_resource(Samjha, generate_url([base_url, '2']))
    api.add_resource(Search, generate_url([base_url, 's']))