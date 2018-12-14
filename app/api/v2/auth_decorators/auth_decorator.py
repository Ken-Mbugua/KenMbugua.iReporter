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
            # extract the token only from [bearer xxxxxxxx]
            access_token = request.headers["Authorization"].split(" ")[1]
            message = UsersModel().decode_auth_token(access_token)
            print("HEADERz:::", message)

        return j(*args, **kwargs)

    return decorated
