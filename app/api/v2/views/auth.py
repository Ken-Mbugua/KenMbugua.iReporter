import json
from flask import request, json
from flask_restful import Resource
from app.api.v2.models.users_model import UsersModel
from app.api.v2.views.validation import ViewsValidation


class AuthSignUp(Resource):

    def post(self):

        data = request.get_json(silent=True)

        if data:  # allow json formated data only

            # check for missing fields
            fields = ['username', 'email', 'password', 'phone_number']
            if not ViewsValidation().check_fields(fields, data):

                # instanciate Users model and pass request data
                user = UsersModel(**data)

                email = user.get_user_by_email(data["email"])

                if email:
                    # duplicate user  error
                    return {
                        "status": 202,
                        "message": "Duplicate User Error"
                    }, 202

                # create user
                response = user.create_user()

                if response:

                    user_details = user.get_user_details(data["email"])
                    user_details.update({"token": "w23502384023-24360808"})
                    return {  # user creation success return user data
                        "status": 201,
                        "data": [
                            user_details
                        ]
                    }, 201

            else:  # found missing fields
                return ViewsValidation().check_fields(fields, data)

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
