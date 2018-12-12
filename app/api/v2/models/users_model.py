import datetime
from flask_bcrypt import generate_password_hash
from app.api.v1.models.models_validation.validation import ModelValidation

from app.db.db_config import DbModel


class UsersModel(DbModel):

    def __init__(self, username=None, firstname=None, email=None,
                 phone_number=None, password=None,
                 isAdmin=False, date_created=None):

        self.firstname = firstname
        self.username = username
        self.email = email
        self.password_hash = generate_password_hash(
            password).decode("utf-8")
        self.isAdmin = isAdmin
        self.phone_number = phone_number
        self.date_created = datetime.datetime.now()

        # instanciate the inherited DbModel class
        super().__init__()

    def create_user(self):

        email = self.get_user_by_email(self.email)

        if email:
            # duplicate user found return None
            return None
        else:
            query_string = "INSERT INTO users(email, username,  " +\
                "phone_number, password_hash) VALUES (%s,%s,%s,%s)"

            data = (self.email, self.username,
                    self.phone_number, self.password_hash,)

            # run query then commit record
            self.query(query_string, data)
            self.save()
            return "create user success"

    def get_user_by_email(self, user_email):

        query = "SELECT * from users WHERE email= %s"
        # query db
        self.query(query, (user_email,))
        # return queried records (single record)
        user = self.find_one()

        if user:
            user_data = dict(
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
