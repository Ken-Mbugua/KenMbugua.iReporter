import datetime
from flask_bcrypt import generate_password_hash

_users_db = []


class UsersModel():

    def __init__(self):
        self.createt_at = datetime.datetime
        self._users_db = _users_db

    def create_user(self, user_details):

        user_details = {
            # implements id auto increment feature
            "id": len(self._users_db)+1,
            "firstname": user_details["firstname"],
            "lastname": user_details["lastname"],
            "othername": user_details["othername"],
            "email": user_details["email"],
            "phonenumber": user_details["phonenumber"],
            "password_hash": generate_password_hash(user_details["password"])
            .decode("utf-8"),
            "isAdmin": False,
            "createdBy": user_details["createdBy"],
            "Registered": str(datetime.datetime.now())
        }

        user = self.get_single_user(user_details["id"])
        if user:
            return None  # user already exists
        else:
            self._users_db.append(user_details)
            return user_details

    def delete_user(self, user_id):
        user = self.get_single_user(user_id)
        if user:
            _users_db.pop(user_id - 1)
            return user
        return None  # user not found

    def update_user(self, user_id, data):
        user = self.get_single_user(user_id)
        if user:
            user.update(data)
            return user
        return None  # user not found

    def get_single_user(self, user_id):
        for user in self._users_db:
            if user.id == user_id:
                return user
        return None  # user not found

    def get_all_users(self):
        if not self._users_db:
            return self._users_db
        return None  # user not found
