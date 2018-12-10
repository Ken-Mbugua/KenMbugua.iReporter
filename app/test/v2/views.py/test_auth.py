
import json
from unittest import TestCase
from app import create_app
from app.db.db_config import DbModel


class TestAuth(TestCase):
    def setUp(self):
        app = create_app("testing")
        self.app = app.test_client()
        self.app_context = app.app_context()
        self.app_context.push()
        self.db = DbModel()

        self.sign_up_data = {
            "email": "user792@gmail.com",
            "password": "user_1#",
            "phone_number": "0958576262",
            "username": "de_jong"
        }

    def signup_user(self, sign_up_data):
        response = self.app.post(
            'api/v2/auth/signup',
            data=json.dumps(self.sign_up_data),
            content_type='application/json'
        )

        return response

    def test_auth_sign_up(self):
        """ Test for user registration """

        response = self.signup_user(self.sign_up_data)
        result = json.loads(response.data.decode())
        print("DATA1:::", result)
        print("result['status']:::", result['status'])
        self.assertTrue(result['status'] == 201)
        self.assertTrue(result['data'])
        print("data length:::", len(result['data']))
        # test for auth token
        self.assertTrue(result['data'][0])
        self.assertTrue(response.content_type == 'application/json')
        self.assertEqual(response.status_code, 201)

    def test_auth_sign_up_duplicate_user(self):
        """ Test for duplicate user registration """

        response = self.signup_user(self.sign_up_data)
        result = json.loads(response.data.decode())
        print("DATA1:::", result)
        self.assertTrue(result['status'] == 400)
        self.assertFalse(result['error'] == "User Already Exists")
        self.assertTrue(response.content_type == 'application/json')
        self.assertEqual(response.status_code, 400)

    def tearDown(self):
        self.db.destroy_tables()
