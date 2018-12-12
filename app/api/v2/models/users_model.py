import datetime
from flask_bcrypt import generate_password_hash
from app.api.v1.models.models_validation.validation import ModelValidation

from app.db.db_config import DbModel


class UsersModel(DbModel):

    def __init__(self, username=None, firstname=None, email=None, phone_number=None,
                 password_hash=None, isAdmin=False,
                 date_created=None):

        self.firstname = firstname
        self.username = username
        self.email = email
        self.password_hash = generate_password_hash
        (user_details["password"])
        .decode("utf-8"),
        self.isAdmin = isAdmin
        self.date_created = datetime.datetime.now()

        # instanciate the inherited DbModel class
        super().__init__()

    # def user_object(self, user_details):
    #     """method to formart user data object"""

    #     return {
    #         "auth_token": "iwtgrsh7772099gavgfhlwe??@@##gafugiuwef&$$",
    #         "user": {
    #             "firstname": "",
    #             "username": user_details["username"],
    #             "email": user_details["email"],
    #             "phone_number": user_details["phone_number"],
    #             "password_hash": generate_password_hash
    #             (user_details["password"])
    #             .decode("utf-8"),
    #             "isAdmin": False,
    #             "createdBy": 34,
    #             "Registered": str(self.date_created)
    #         }
    #     }

    def user_res_object(self, user_details):
        """method to formart user data object"""

        return {
            "auth_token": "iwtgrsh7772099gavgfhlwe??@@##gafugiuwef&$$",
            "user": {
                "firstname": "",
                "username": user_details["username"],
                "email": user_details["email"],
                "phone_number": user_details["phone_number"],
                "Registered": str(self.date_created)
            }
        }

    def create_user(self, user_details):

        user_details = self.user_object(user_details)

        # print("User_details::", user_details)
        # print("Email::", user_details["user"]["email"])

        email = self.get_user_by_email(user_details["user"]["email"])

        if email:  # duplicate user found return None
            return None
        else:
            query = "INSERT INTO users(email, username, phone_number, " +\
                " password_hash, auth_token) VALUES (" +\
                " '"+(user_details["user"]["email"]+"', " +
                      " '"+user_details["user"]["username"]+"', " +
                      " '"+user_details["user"]["phone_number"]+"', " +
                      " '"+user_details["user"]["password_hash"]+"', " +
                      " '"+user_details["auth_token"])+"') "

            # run query then commit record
            self.query(query)
            self.save()
            return user_details

    def get_user_by_email(self, user_email):

        query = "SELECT * from users WHERE email='"+user_email+"'"
        # query db
        self.query(query)
        # return queried records (single record)
        user = self.find_one()

        if user:
            user_data = dict(
                token=user[1],
                user=dict(
                    username=user[2],
                    date_created="{}".format(user[9])
                )
            )
            return user_data
        return None  # user not found

    # def get_all_users(self):
    #     if not self.find_all():
    #         return None
    #     return self.find_all()  # user not found

    def gen_auth_token(self, user_email):
        pass

    def decode_auth_token(self):
        pass
