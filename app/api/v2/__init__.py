from flask import Blueprint
from flask_restful import Api

# defining new v2 blueprint
version_two = Blueprint('ap1_v2', __name__, url_prefix='api/v2')
api = Api(version_two)

# define endpoints here

# api.add_resource(ViewResource, '/incidents')
