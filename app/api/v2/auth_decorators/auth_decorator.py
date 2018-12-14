import jwt
from functools import wraps
from app.api.v2.models.users_model import UsersModel
from flask_restful import request


def isAdmin(j):
    @wraps(j)
    def decorated(*args, **kwargs):
        access_token = None
        message = None

        if "Authorization" in request.headers:
            print("HEADERz:::", request.headers)

        return j(*args, **kwargs)

    return decorated
