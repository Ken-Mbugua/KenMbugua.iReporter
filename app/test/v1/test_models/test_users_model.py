from unittest import TestCase
from app.api.v1.models.users_model import UsersModel


class TestUsersModel(TestCase):
    def setUp(self):
        self.user = UsersModel()
        self.user_data = self.user._users_db
        user_data = {

        }

    def create_test_user(self):
        return self.user.create_user(user_data)

    def test_create_user(self):

    def tearDown(self):
        self.user_data.clear()
