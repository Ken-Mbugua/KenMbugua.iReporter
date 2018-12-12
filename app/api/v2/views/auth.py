import json
from flask import request, json
from flask_restful import Resource
from app.api.v2.models.users_model import UsersModel


class AuthSignUp(Resource):

    def post(self):

        data = request.get_json()

        # instanciate Users model and pass request data
        user = UsersModel(**data)

        response = user.create_user()

        if response:
            return {  # user creation success
                "status": 201,
                "data": [response]
            }, 201
        else:
            return {  # bad request error  # duplicate user error
                "status": 400,
                "error": "User Already Exists"
            }, 400


class AuthSignIn(Resource):

    def post(self):  # login resource

        data = request.get_json()

        user = UsersModel()  # instanciate Users model
        res = user.get_user_by_email(data["email"])

        # print("RESPONSE:: ", res)

        if res:
            return {
                "status": 200,
                "message": "Login Success",
                "data": [res]
            }, 200
        else:
            return {
                "status": 401,
                "error": "Unregistered User"
            }, 401
