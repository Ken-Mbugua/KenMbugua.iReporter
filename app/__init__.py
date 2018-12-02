from flask import Blueprint
from flask_restful import Api

"""
blueprints initialises in v1

"""
version_one = Blueprint('api_v1', __name__, url_prefix='/api/v1')
api = Api(version_one)
