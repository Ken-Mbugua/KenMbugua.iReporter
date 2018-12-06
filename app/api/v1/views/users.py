from flask_restful import Resource
import datetime
from flask import request
from app.api.v1.models.users_model import UsersModel
from .views_validation.validation import ViewsValidation


class Users(Resource, UsersModel):
    def __init__(self):
        self._userz = UsersModel()
        self._views_validation = ViewsValidation()

    def post(self):
        """
        method to receive user data and pass to db model save()
        """
        data = request.get_json()
        # validate received fileds
        fields_validate = ViewsValidation()
        fields = [
            'firstname',
            'lastname',
            'email',
            'phonenumber',
            'username',
            'othernames',
            'password'
        ]
        missing_fields = fields_validate.missing_fields(fields, data)

        if not missing_fields:  # filter missing fields
            user_entry = {
                "firstname": data["firstname"],
                "lastname": data["lastname"],
                "email": data["email"],
                "phonenumber": data["phonenumber"],
                "username": data["username"],
                "othernames": data["othernames"],
                "password": data['password'],
                "createdBy": len(['title'])
            }

            res = self._userz.create_user(user_entry)
            print("RES:::", res)
            if res:
                if res["status"] == 400:
                    return res
                else:
                    return {
                        "status": 201,
                        "data": [{
                            "id": res["id"],
                            "message": "user record has been created"
                        }]
                    }, 201
            else:
                return {
                    "status": 400,
                    "error": "Bad Request"
                }, 400
        else:
            return {
                "status": 403,
                "error": "Bad request: missing"
                " fileds {}".format(missing_fields)
            }, 403

    def get(self):
        """
        method to query all incidences from db
        """
        res = self._userz.get_all_users()
        if res:
            return {
                "status": 200,
                "data": res
            }, 200
        else:
            return {
                "status": 404,
                "error": "No users found"
            }, 404


class UsersId(Resource, UsersModel):
    def __init__(self):
        self._user = UsersModel()

    def get(self, user_id):
        """
        method to handle GET single user request
        """
        res = self._user.get_single_user(user_id)

        if res:
            return {
                "status": 200,
                "data": [res]
            }, 200
        else:
            return {
                "status": 404,
                "error": "user with id {} "
                "was not found ".format(user_id)
            }, 404

    def delete(self, user_id):
        """
        method to handle DELETE single user request
        """
        res = self._user.delete_user(user_id)

        if res:
            return {
                "status": 200,
                "data": [{
                    "id": res["id"],
                    "message": "user record has been deleted"
                }]
            }, 200
        else:
            return {
                "status": 404,
                "error": "Not found for id {}".format(user_id)
            }, 404

    def patch(self, user_id):
        """
        method to handle PATCH sigle user request
        any field provided can be updated here
        """

        data = request.get_json()

        res = self._user.update_user(user_id, data)

        if res:
            return {
                "status": 200,
                "data": [{
                    "id": res["id"],
                    "message": "user record has been updated"
                }]
            }, 200
        else:
            return {
                "status": 404,
                "error": "Not found for id {}".format(user_id)
            }, 404
