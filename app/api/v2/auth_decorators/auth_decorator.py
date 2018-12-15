import jwt
from functools import wraps
from app.api.v2.models.users_model import UsersModel
from flask_restful import request


def isAdmin(j):
    @wraps(j)
    def decorated(*args, **kwargs):
        access_token = None
        subject = None

        if "Authorization" in request.headers:
            # extract the token only from [bearer xxxxxxxx]
            access_token = request.headers["Authorization"].split(" ")[1]
            subject = UsersModel().decode_auth_token(access_token)

        if not access_token:
            return {"message": "Please provide a token"}, 401
        if subject.get('invalid-error', None):
            return {"message": subject["invalid-error"]}, 401
        if subject.get('expired-error', None):
            return {"message": subject["expired-error"]}, 401
        if not subject.get('role', None):
            return {"message": "You are a peasant"}, 401

        return j(*args, **kwargs)

    return decorated


def isAuthenticated(j):
    @wraps(j)
    def decorated(*args, **kwargs):
        access_token = None
        subject = None

        if "Authorization" in request.headers:
            # extract the token only from [bearer xxxxxxxx]
            access_token = request.headers["Authorization"].split(" ")[1]
            subject = UsersModel().decode_auth_token(access_token)

        if not access_token:
            return {"message": "Please provide a token"}, 401
        if subject.get('invalid-error'):
            return {"message": subject["invalid-error"]}, 401
        if subject.get('expired-error'):
            return {"message": subject["expired-error"]}, 401

        return j(*args, **kwargs)

    return decorated
