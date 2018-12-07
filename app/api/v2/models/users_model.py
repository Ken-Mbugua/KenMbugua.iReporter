import datetime
from flask_bcrypt import generate_password_hash
from app.api.v1.models.models_validation.validation import ModelValidation

from app.db.db_config import DbModel


class UsersModel():

    def __init__(self):
        self.created_at = datetime.datetime.now()
        self._users_db = DbModel()
        self.model_val = ModelValidation()

    def create_user(self, user_details):

        user_details = {
            "firstname": user_details["firstname"],
            "lastname": user_details["lastname"],
            "othernames": user_details["othernames"],
            "email": user_details["email"],
            "phonenumber": user_details["phonenumber"],
            "password_hash": generate_password_hash(user_details["password"])
            .decode("utf-8"),
            "isAdmin": False,
            "createdBy": user_details["createdBy"],
            "Registered": str(self.created_at)
        }

        email = self.get_user_by_email(user_details["email"])

        if email:  # duplicate user found return
            # duplicate record error
            query_result = self.model_val.models_error(
                400, "User Already Exists")
            return query_result
        else:
            self._users_db.query(user_details)
            user_details["status"] = 200
            return user_details

    def delete_user(self, user_id):
        user = self.get_user_by_id(user_id)
        if user:
            self._users_db.pop(user_id - 1)
            return user
        return None  # user not found

    def update_user(self, user_id, data):
        user = self.get_user_by_id(user_id)
        if user:
            user.update(data)
            return user
        return None  # user not found

    # def get_user_by_id(self, user_id):
    #     for user in self._users_db:
    #         if (user_id == user["id"]):
    #             return user
    #     return None  # user not found

    def get_user_by_email(self, user_email):

        query = "SELECT email FROM users WHERE email={}".format(user_email)
        user = self._users_db.query(query)
        if user:
            return user
        return None  # user not found

    def get_all_users(self):
        if not self._users_db:
            return None
        return self._users_db  # user not found
