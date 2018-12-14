import json
from flask import request, json
from flask_restful import Resource
from app.api.v2.models.users_model import UsersModel
from app.api.v2.views.validation import ViewsValidation
from app.api.v2.auth_decorators.auth_decorator import isAdmin


class AuthSignUp(Resource):

    def post(self):

        data = request.get_json(silent=True)

        if not data:  # allow json formated data only

            return ViewsValidation().views_error(
                400, "Bad Request Format")

        # check for missing fields
        fields = ['username', 'email', 'password', 'phone_number']
        if ViewsValidation().check_fields(fields, data):
            # found missing fields
            return ViewsValidation().check_fields(fields, data)

        # instanciate Users model and pass request data
        user = UsersModel(**data)

        email = user.get_user_by_email(data["email"])

        if email:
            # duplicate user  error
            return ViewsValidation().views_error(
                202, "Duplicate User Error", "message")

        # create user
        response = user.create_user()

        if response:
            user_details = user.get_user_details(data["email"])
            # generate token
            auth_token = user.gen_auth_token(data["email"])

            # user.decode_auth_token(auth_token)["role"]
            # returns role or email

            user_details.update({"token": auth_token.decode()})
            return {  # user creation success return user data
                "status": 201,
                "data": [
                    user_details
                ]
            }, 201


class AuthSignIn(Resource):

    def post(self):  # login resource

        data = request.get_json(silent=True)

        if not data:  # allow json formated data only
            # bad request format error
            return ViewsValidation().views_error(400, "Bad Request Format")

        fields = ['email', 'password']
        # check for missing fields
        if ViewsValidation().check_fields(fields, data):
            # found missing fields
            return ViewsValidation().check_fields(fields, data)

        # instanciate Users model and pass request data
        user = UsersModel(**data)

        email = user.get_user_by_email(data["email"])

        if email:
            # user found check password
            if user.password_is_valid(data["password"]):
                # login success: get user details
                user_details = user.get_user_details(data["email"])
                # generete token
                auth_token = user.gen_auth_token(data["email"])
                user_details.update({"token": auth_token.decode()})

                return {  # user login success return token and suser data
                    "status": 200,
                    "data": [
                        user_details
                    ]
                }, 200

            else:
                return ViewsValidation().views_error(
                    401, "Invalid Login credentials", "message")
        else:
            return ViewsValidation().views_error(
                401, "User with email {} not found ".format(data["email"]),
                "message")
