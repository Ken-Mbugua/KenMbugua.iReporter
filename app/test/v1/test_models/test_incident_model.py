import unittest
import datetime
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

        self.current_time = str(datetime.datetime.now())
        self.maxDiff = None
        self.incident_entry = {
            "title": "Traffice Corruption",
            "description": "Offices taking bribes",
            "type": "RedFlag",
            "incident_status": "Rejected",
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
            "createdBy": 24
        }

        self.insert_result = {
            'id': 1,
            'title': 'Traffice Corruption',
            'description': 'Offices taking bribes',
            'location': '-34444400, 3444499900',
            'incident_status': 'Rejected',
            'image': [{'dir': 'var/www/uploads/incidents/img/USR-232455.jpeg',
                       'filesize': '2045kb'},
                      {'dir': 'var/www/uploads/incidents/img/USR-232455.jpeg',
                       'filesize': '2045kb'}],
            'video': [
                {'dir': 'var/www/uploads/readflags/video/USR-232455.mp4',
                    'filesize': '340098245Kb'},
                {'dir': 'var/www/uploads/readflags/video/USR-232455.mp4',
                 'filesize': '340098245Kb'}],
            'comment': 'This is fake all news i tell ya',
            'createdBy': 24,
            'createdOn': '2018-12-06 11:13:51.573138',
            'status': 200
        }

        # self.insert_record(self.incident_entry)
        # print(self.incident_entry["createdBy"])

    def insert_record(self):
        self.incident.save(self.incident_entry)

    def test_save_incident(self):
        test_incident = self.incident.save(self.incident_entry)
        self.assertEqual(test_incident["comment"],
                         "This is fake all news i tell ya")

    def test_delete_incident(self):
        print(self.incident._dbase)
        test_incident = self.incident.delete_incident(1)
        self.assertIsNone(test_incident)

    def test_edit_incident(self):
        self.insert_record()
        test_incident = self.incident.edit_incident(
            1, {"incident_status": "Resolved"})
        self.assertAlmostEqual(test_incident["incident_status"], "Resolved")

    def test_get_incident(self):
        # return none since incidents = empty
        test_incident = self.incident.get_incident_by_id(1)
        self.assertIsNone(test_incident)

        # insert record
        self.insert_record()

        test_incident = self.incident.get_incident_by_id(1)
        self.assertIsNotNone(test_incident)

    def test_get_incidents(self):
        # return none since incidents = empty
        test_incident = self.incident.get_incidents()
        self.assertIsNone(test_incident)

        # insert record
        self.insert_record()

        test_incident = self.incident.get_incidents()
        self.assertIsNotNone(test_incident)

    def tearDown(self):
        self.incident._dbase.clear()
