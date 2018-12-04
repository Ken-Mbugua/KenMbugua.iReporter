import datetime


class UsersModel:
    _users_db = []

    def __init__(self):
        self.createt_at = datetime.datetime

    def create_user(self, user_details):
        return user_details

    def delete_user(self, user_id):
        return self._users_db

    def update_user(self, user_id):
        return self._users_db

    def get_single_user(self, user_id):
        return self._users_db
