from .views import HelloWorld, Samjha

def initialize_routes(api):
    api.add_resource(HelloWorld, '/')
    api.add_resource(Samjha, '/samjha')