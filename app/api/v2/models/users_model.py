import jwt
from app.db.db_config import DbModel
from datetime import datetime, timedelta
from flask_bcrypt import generate_password_hash, check_password_hash
from app.api.v1.models.models_validation.validation import ModelValidation
from flask import current_app


class UsersModel(DbModel):

    def __init__(self, username=None, firstname=None, email=None,
                 phone_number=None, password=None,
                 isAdmin=False, date_created=None):

        self.firstname = firstname
        self.username = username
        self.email = email
        self.password = "user34" if password is None else password
        self.password_hash = generate_password_hash(
            self.password).decode("utf-8")
        self.isAdmin = isAdmin
        self.phone_number = phone_number
        self.date_created = datetime.utcnow()

        # instanciate the inherited DbModel class
        super().__init__()

    def create_user(self):

        query_string = "INSERT INTO users(email, username,  " +\
            "phone_number, password_hash, is_admin) VALUES (%s,%s,%s,%s,%s)"

        data = (self.email, self.username,
                self.phone_number, self.password_hash, self.isAdmin,)

        # run query then commit record
        self.query(query_string, data)
        self.save()

        return {"message": "record saved successsfully"}

    def get_user_by_email(self, user_email):

        query = "SELECT * from users WHERE email= %s"
        # query db
        self.query(query, (user_email,))
        # return queried records (single record)
        user = self.find_one()

        if user:
            return user
        return None  # user not found

    def get_user_details(self, user_email):

        user = self.get_user_by_email(user_email)
        # print("USER::::", user)
        if user:
            return dict(
                user=dict(
                    username=user[1],
                    email=user[2],
                    phone_number=user[6],
                    date_created="{}".format(user[8])
                )
            )
        return None  # user not found

    def password_is_valid(self, password):
        user = self.get_user_by_email(self.email)
        password_hash = user[3]

        if check_password_hash(password_hash, password):
            return True
        else:
            return None

    def gen_auth_token(self, user_email):
        try:
            payload = {
                'exp': datetime.utcnow() + timedelta(days=0, minutes=25),
                'isa': "{}".format(datetime.utcnow()),
                'email': user_email,
                'role': self.isAdmin
            }
            return jwt.encode(
                payload,
                current_app.config['SECRET_KEY'],
                algorithm='HS256'
            )
        except Exception as error:
            return error

    @staticmethod
    def decode_auth_token(auth_token):
        """decode auth_token to obtain payload data"""

        try:
            payload = jwt.decode(
                auth_token,
                current_app.config['SECRET_KEY'],
                algorithms='HS256'
            )

            return {
                "email": payload['email'],
                "role": payload['role']
            }

        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'
