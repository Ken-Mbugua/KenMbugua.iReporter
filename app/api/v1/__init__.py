from flask import Blueprint
from flask_restful import Api

# imported Incidents from views
from .views.incidents import Incidents

version_one = Blueprint('api_v1', __name__, url_prefix='/api/v1')
api = Api(version_one)

# incidents end point
api.add_resource(Incidents, '/incidents', endpoint='incidents_list')
