import datetime
from flask_bcrypt import generate_password_hash
from .models_validation.validation import ModelValidation

_users_db = []


class UsersModel():

    def __init__(self):
        self.created_at = datetime.datetime.now()
        self._users_db = _users_db
        self.model_val = ModelValidation()

    def create_user(self, user_details):
        user_details = {
            # implements id auto increment feature
            # get last record id then increment by 1
            "id": self.auto_increment(),
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

        if_user = self.get_user_by_id(user_details["id"])
        if_email = self.get_user_by_email(user_details["email"])

        if if_user or if_email:  # duplicate user found return
            # duplicate record error
            query_result = self.model_val.models_error(
                400, "User Already Exists")
            return query_result
        else:
            self._users_db.append(user_details)
            user_details["status"] = 200
            return user_details

    def delete_user(self, user_id):
        user = self.get_user_by_id(user_id)
        if user:
            _users_db.pop(user_id - 1)
            return user
        return None  # user not found

    def update_user(self, user_id, data):
        user = self.get_user_by_id(user_id)
        if user:
            user.update(data)
            return user
        return None  # user not found

    def get_user_by_id(self, user_id):
        for user in self._users_db:
            if (user_id == user["id"]):
                return user
        return None  # user not found

    def get_user_by_email(self, user_email):
        for user in self._users_db:
            if (user_email == user["email"]):
                return user
        return None  # user not found

    def get_all_users(self):
        if not self._users_db:
            return None
        return self._users_db  # user not found

    def auto_increment(self):
        if not self._users_db:
            return len(self._users_db)+1
        else:
            return (self._users_db[-1]["id"])+1
