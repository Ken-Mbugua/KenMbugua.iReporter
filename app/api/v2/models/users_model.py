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
            "email": user_details["email"],
            "phone_number": user_details["phone_number"],
            "password_hash": generate_password_hash(user_details["password"])
            .decode("utf-8"),
            "isAdmin": False,
            "createdBy": 34,
            "Registered": str(self.created_at),
            "demo_token": "iwtgrsh7772099gavgfhlwe??@@##gafugiuwef&$$"
        }

        email = self.get_user_by_email(user_details["email"])

        if email:  # duplicate user found return
            # duplicate record error
            return None
        else:
            query = "INSERT INTO users(email, phone_number, password_hash, " +\
                " auth_token) VALUES (" +\
                " '"+(user_details["email"]+"', " +
                      " '"+user_details["phone_number"]+"', " +
                      " '"+user_details["password_hash"]+"', " +
                      " '"+user_details["demo_token"])+"') "

            print("INSERT QUERY ", type(query))

            # hope it doesnt crash here
            self._users_db.query(query)
            self._users_db.save()
            return {"status": 201, "message": "User created successesfully"}

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
