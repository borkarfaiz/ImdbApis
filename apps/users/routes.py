from utils import generate_url
from .views import SignUp, Token, TokenRefresh


def user_routes(api, base_url):
    api.add_resource(SignUp, generate_url([base_url, 'sign_up']))
    api.add_resource(Token, generate_url([base_url, 'token']))
    api.add_resource(TokenRefresh, generate_url([base_url, 'token/refresh']))
