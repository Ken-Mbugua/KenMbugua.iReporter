from flask import request, json
from flask_restful import Resource
from app.api.v2.models.users_model import UsersModel


class AuthSignUp(Resource):
    def __init__(self):
        self._signup = UsersModel()

    def post(self):

        data = request.get_json()

        res = self._signup.create_user(data)

        if res:
            if res['error']:  # duplicate user error
                return res, 400
            else:
                return {  # user creation success
                    "status": 201,
                    "data": [res]
                }, 201
        else:
            return {  # bad request error
                "status": 403,
                "error": "Bad Request"
            }, 403


class AuthSignIn(Resource):
    def __init__(self):
        self._signin = UsersModel()

    def post(self):  # get users by id

        data = request.get_json()

        res = self._signin.get_user_by_email(data["email"])

        if res:
            return {
                "status": 200,
                "message": "Login Success"
            }, 200
        else:
            return {
                "status": 400,
                "error": "Bad Request"
            }, 400
