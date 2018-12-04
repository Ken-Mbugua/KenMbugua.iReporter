from unittest import TestCase
import datetime
from app.api.v1.models.users_model import UsersModel


class TestUsersModel(TestCase):
    def setUp(self):
        self.user = UsersModel()
        self.user_data = self.user._users_db
        self.user_data = {
            "firstname": "Andeka",
            "lastname": "Kibiro",
            "othernames": "AnKibi",
            "email": "ankibi@andela.com",
            "phoneNumber": "07168858858",
            "username": "@Ankibi",
            "registered": str(datetime.datetime.now()),
            "isAdmin": "False"
        }

    def create_test_user(self):
        return self.user.create_user(self.user_data)

    def test_create_user(self):

    def tearDown(self):
        self.user_data.clear()
