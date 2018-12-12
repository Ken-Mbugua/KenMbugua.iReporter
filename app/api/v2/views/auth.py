import json
from flask import request, json
from flask_restful import Resource
from app.api.v2.models.users_model import UsersModel


class AuthSignUp(Resource):

    def post(self):

        data = request.get_json(silent=True)

        if data:  # alllow json formated data only

            # instanciate Users model and pass request data
            user = UsersModel(**data)

            email = user.get_user_by_email(data["email"])

            if email:
                # duplicate user found return
                return {  # user creation success
                    "status": 202,
                    "message": "Duplicate User Error"
                }, 202

            try:
                # create user
                response = user.create_user()

                if response:
                    return {  # user creation success
                        "status": 201,
                        "data": [{
                            "token": "oirutonnvsoo3424592jsofhsf03wrj",
                            response
                        }]
                    }, 201

            except Exception as err:
                return {  # bad request error
                    "status": 400,
                    "error": "Bad Request: "+err
                }, 400

        else:
            return {  # bad request format error
                "status": 403,
                "error": "Bad Request Format"
            }, 403


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
