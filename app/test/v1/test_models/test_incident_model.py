import unittest
import json
import os

# import create app
from app import create_app
# import incident_model from models
from app.api.v1.models.incidents_model import IncidentsModel

app = create_app("testing")


class TestIncidentsModel(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.incident = IncidentsModel()
        self.app_context = app.app_context()
        self.app_context.push()

        self.incident_entry = {
            "title": "Traffice Corruption",
            "description": "Offices taking bribes",
            "type": "RedFlag",
            "status": "Rejected",
            "location": "-34444400, 3444499900",
            "image": [
                {
                      "dir": "var/www/uploads/incidents/img/USR-232455.jpeg",
                      "filesize": "2045kb"
                },
                {
                    "dir": "var/www/uploads/incidents/img/USR-232455.jpeg",
                    "filesize": "2045kb"
                }
            ],
            "video": [
                {
                    "dir": "var/www/uploads/readflags/video/USR-232455.mp4",
                    "filesize": "340098245Kb"
                }, {
                    "dir": "var/www/uploads/readflags/video/USR-232455.mp4",
                    "filesize": "340098245Kb"
                }
            ],
            "comment": "This is fake all news i tell ya",
            "createdBy": 30
        }

    def test_save_incident(self):
        self.assertEqual(self.incident.save(self.incident_entry), True)

    def test_delete_incident(self):
        pass

    def test_edit_incident(self):
        pass

    def test_get_incident(self):
        pass

    def test_get_incidents(self):
        pass

    def tearDown(self):
        pass
