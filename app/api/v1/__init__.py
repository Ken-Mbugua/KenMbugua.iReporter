from flask import Blueprint
from flask_restful import Api

# imported Incidents from views
from .views.incidents import Incidents, IncidentsId
from .views.update_incident import IncidentsUpdateLocation
from .views.update_incident import IncidentsUpdateComment
from .views.users import Users, UsersId

version_one = Blueprint('api_v1', __name__, url_prefix='/api/v1')
api = Api(version_one)

# incidents end points
api.add_resource(Incidents, '/incidents', endpoint='incidents_list')
api.add_resource(IncidentsId, '/incidents/<int:incident_id>',
                 endpoint='incident')
api.add_resource(IncidentsUpdateLocation,
                 '/incidents/<int:incident_id>/location')
api.add_resource(IncidentsUpdateComment,
                 '/incidents/<int:incident_id>/comment')

api.add_resource(Users, '/users', endpoint='users_list')
api.add_resource(UsersId, '/users/<int:incident_id>',
                 endpoint='user')
