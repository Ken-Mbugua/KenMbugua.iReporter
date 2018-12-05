import datetime

_users_db = []


class UsersModel:

    def __init__(self):
        self.createt_at = datetime.datetime
        self._users_db = _users_db

    def create_user(self, user_details):
        _users_db.append(user_details)
        return user_details

    def delete_user(self, user_id):
        user = self.get_single_user(user_id)
        if user:
            _users_db.pop(user_id - 1)
            return self._users_db
        return None

    def update_user(self, user_id):
        user = self.get_single_user(user_id)
        if user:
            _users_db.pop(user_id - 1)
            return self._users_db
        return None

    def get_single_user(self, user_id):
        for user in self._users_db:
            if user.id == user_id:
                return user
        return None
