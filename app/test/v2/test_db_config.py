from unittest import TestCase

from app.db.db_config import DbModel

from app import create_app


class TestDbModel(TestCase):
    """
    class to test Db connection class Db config
    """

    def setUp(self):
        app = create_app("testing")
        self.app = app.test_client()
        self.app_context = app.app_context()
        self.app_context.push()
        self.dbase = DbModel()

    def test_create_tables(self):
        """
        test to see if table is created,
        returns none if executes
        """
        self.assertEqual(
            self.dbase.create_tables(),
            None,
            "Created tables Successfully"
        )

    def test_query(self):
        """
        test to see if query executes,
        returns none if executes
        """
        self.assertEqual(
            self.dbase.query("SELECT * FROM users"),
            None,
            "creation table incidents success"
        )

        self.assertEqual(
            self.dbase.query("SELECT * FROM incidents"),
            None,
            "creation table incidents success"
        )
