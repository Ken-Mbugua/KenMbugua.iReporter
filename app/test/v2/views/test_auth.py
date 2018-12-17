
import json
from unittest import TestCase
from app import create_app
from app.db.db_config import DbModel
from app.api.v2.models.users_model import UsersModel
from test_data_auth import sign_in_data, sign_in_data_2, sign_up_data, \
    sign_in_seeded_admin


class TestAuth(TestCase):
    """ Test class for sign up and sign in enpoints"""

    def setUp(self):
        app = create_app("testing")
        self.app = app.test_client()
        self.app_context = app.app_context()
        self.app_context.push()
        self.db = DbModel()

    def signup_user(self, sign_up_data):
        response = self.app.post(
            'api/v2/auth/signup',
            data=json.dumps(sign_up_data),
            headers={"Content-Type": "application/json"}
        )

        return response

    def signin_user(self, sign_in_data):
        response = self.app.post(
            'api/v2/auth/login',
            data=json.dumps(sign_in_data),
            headers={
                "Content-Type": "application/json"
            }
        )

        return response

    def get_user(self, sign_in_data):
        # sign in
        self.signin_user(sign_in_data)

        # instanciate user
        user = UsersModel(
            email=sign_in_data["email"],
            password=sign_in_data["password"]
        )

        return user

    def test_auth_sign_up(self):
        """ Test for user registration """

        response = self.signup_user(sign_up_data)
        result = json.loads(response.data.decode())

        self.assertTrue(result['data'])

        # test for auth token
        self.assertTrue(result['data'][0]['token'])
        self.assertEqual(response.status_code, 201)

    def test_auth_sign_up_duplicate_user(self):
        """ Test for duplicate user registration """

        # sign up user attempt 1 -> success
        self.signup_user(sign_up_data)

        # sign up user attempt 2 -> failure
        response = self.signup_user(sign_up_data)

        result = json.loads(response.data.decode())

        self.assertEqual(result['message'], "Duplicate User Error")
        self.assertEqual(response.status_code, 202)

    def test_auth_sign_in(self):
        """ Test for user login endpoint """
        # create a new user
        self.signup_user(sign_up_data)

        # sign in with the user created above
        response = self.signin_user(sign_in_data)

        result = json.loads(response.data.decode())

        self.assertEqual(len(result['data']), 1)

        # test for auth token
        self.assertTrue(result['data'][0]['token'])
        self.assertEqual(response.status_code, 200)

    def test_auth_guest_sign_in(self):
        """ Test for user login endpoint """
        # user sign in
        response = self.signin_user(sign_in_data)

        result = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 401)
        self.assertEqual(
            "User with email {} not found".format(
                sign_in_data["email"]),
            result["message"]
        )

    def test_password_is_valid(self):
        pass

    def test_gen_auth_token(self):
        """ test for generated tokem """

        # get token
        user = self.get_user(
            sign_in_data
        )

        # get token
        auth_token = user.gen_auth_token(sign_in_data["email"])

        # test for token datatype (bytes)
        self.assertTrue(isinstance(auth_token, bytes))

    def test_decode_auth_token(self):

        # get token
        user = self.get_user(
            sign_in_data
        )

        # get token
        auth_token = user.gen_auth_token(sign_in_data["email"])

        # assert token datatype (bytes)
        self.assertTrue(isinstance(auth_token, bytes))

        # test passes if the email used to encode is returned
        self.assertEqual(user.decode_auth_token(
            auth_token)["email"], sign_in_data["email"])

    def tearDown(self):
        """empty table data after each test"""
        self.db.truncate_tables()
