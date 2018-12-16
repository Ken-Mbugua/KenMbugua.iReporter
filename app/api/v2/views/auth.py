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
            return {
                "status": 200,
                "message": "user added successfully"
            }
        else:
            return {
                "status": 400,
                "error": "Bad Request"
            }


# class AuthSignIn(Resource):
#     def __init__(self):
#         self._signin = UsersModel()
