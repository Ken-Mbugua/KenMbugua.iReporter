from flask import Blueprint
from flask_restful import Api

# imported Incidents from views
from .views.incidents import Incidents, IncidentsId

version_one = Blueprint('api_v1', __name__, url_prefix='/api/v1')
api = Api(version_one)

# incidents end points
api.add_resource(Incidents, '/incidents', endpoint='incidents_list')
api.add_resource(IncidentsId, '/incidents/<int:incident_id>',
                 endpoint='incident')
