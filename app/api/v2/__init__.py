from flask import Blueprint
from flask_restful import Api


from app.api.v2.views.auth import AuthSignUp, AuthSignIn
from app.api.v2.views.incidents import Incidents, IncidentsID, IncidentsPatch
from app.api.v2.views.admin_incidents import IncidentsAdmin

# defining new v2 blueprint
version_two = Blueprint('ap1_v2', __name__, url_prefix='/api/v2')
api = Api(version_two)

# define endpoints here

api.add_resource(AuthSignUp, '/auth/signup')
api.add_resource(AuthSignIn, '/auth/login')
api.add_resource(Incidents, '/<incident_type>')
api.add_resource(IncidentsID, '/<incident_type>/<incident_id>')
api.add_resource(IncidentsPatch, '/<incident_type>/<incident_id>/<field>')
api.add_resource(IncidentsAdmin, '/<incident_type>/<incident_id>/status')
# /redflags/34/comment
