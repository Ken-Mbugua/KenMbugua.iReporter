import datetime
from flask_bcrypt import generate_password_hash
from app.api.v1.models.models_validation.validation import ModelValidation

from app.db.db_config import DbModel


class UsersModel():

    def __init__(self):
        self.created_at = datetime.datetime.now()
        self._users_db = DbModel()
        self.model_val = ModelValidation()

    def user_details(self, user_details):
        return {
            "email": user_details["email"],
            "phone_number": user_details["phone_number"],
            "password_hash": generate_password_hash(user_details["password"])
            .decode("utf-8"),
            "username": user_details["username"],
            "isAdmin": False,
            "createdBy": 34,
            "Registered": str(self.created_at),
            "demo_token": "iwtgrsh7772099gavgfhlwe??@@##gafugiuwef&$$"
        }

    def create_user(self, user_details):

        print("User_details::", user_details)

        email = self.get_user_by_email(user_details["email"])

        if email:  # duplicate user found return
            return None
        else:
            query = "INSERT INTO users(email, username, phone_number, " +\
                " password_hash, auth_token) VALUES (" +\
                " '"+(user_details["email"]+"', " +
                      " '"+user_details["username"]+"', " +
                      " '"+user_details["phone_number"]+"', " +
                      " '"+user_details["password_hash"]+"', " +
                      " '"+user_details["demo_token"])+"') "

            # run query then commit record
            self._users_db.query(query)
            self._users_db.save()
            return user_details

    def delete_user(self, user_id):
        query = "DELETE FROM users WHERE id='"+user_id+"'"
        # query db
        self._users_db.query(query).save()
        # return queried records (single record)
        user = self._users_db.find_one()
        if not user:
            return {"status": 204, "msg": "deleted user successfully"}
        return None  # user not found

    def get_user_by_email(self, user_email):

        query = "SELECT * from users WHERE email='"+user_email+"'"
        # query db
        self._users_db.query(query)
        # return queried records (single record)
        user = self._users_db.find_one()

        if user:
            return user
        return None  # user not found

    def get_all_users(self):
        if not self._users_db:
            return None
        return self._users_db  # user not found

    def gen_auth_token(self, user_email):
        pass

    def decode_auth_token(self):
        pass
