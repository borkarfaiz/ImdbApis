from .views import HelloWorld, Samjha, Search

def initialize_routes(api):
    api.add_resource(HelloWorld, '/')
    api.add_resource(Samjha, '/samjha')
    api.add_resource(Search, '/s')