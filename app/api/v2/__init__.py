from flask import Blueprint
from flask_restful import Api


from app.api.v2.views.auth import AuthSignUp, AuthSignIn
from app.api.v2.views.incidents import Incidents

# defining new v2 blueprint
version_two = Blueprint('ap1_v2', __name__, url_prefix='/api/v2')
api = Api(version_two)

# define endpoints here

api.add_resource(AuthSignUp, '/auth/signup')
api.add_resource(AuthSignIn, '/auth/login')
api.add_resource(Incidents, '/redflags')
api.add_resource(Incidents, '/interventions')
