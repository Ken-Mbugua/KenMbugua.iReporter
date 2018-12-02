import os
from unittest import TestCase
import json

from app import create_app
from instance.config import app_config

CONFIG_NAME = app_config['testing']
app = create_app(CONFIG_NAME)


class TestIncidents(TestCase):
    def setUp(self):
        self.app = app.test_client()
        # app.testing = True
        self.app_context = app.app_context()
        self.app_context.push()
        self.incident1 = {
            "title": "Traffice Corruption",
            "description": "Offices taking bribes",
            "type": "RedFlag",
            "status": "Rejected",
            "location": "-34444400, 3444499900",
            "image":
            "[{'path':'var/www/uploads/incidents/img/USR-232455.jpeg'}]",
            "video": "[var/www/uploads/readflags/video/USR-232455]",
            "comment": "This is fake all news i tell ya"
        }

        self.incident2 = {
            "title": "Traffice Corruption",
            "description": "Offices taking bribes",
            "type": "RedFlag",
            "status": "Rejected",
            "location": "-34444400, 3444499900",
            "image":
            "[{'path':'var/www/uploads/incidents/img/USR-232455.jpeg'}]",
            "video": "[var/www/uploads/readflags/video/USR-232455]",
            "comment": "This is fake all news i tell ya"
        }

    def test_get_inicident(self):
        response = self.app.get('/api/v1/incidents')
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(result["status"], 200)

    def test_create_incident(self):
        response = self.app.post('/api/v1/incidents')
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(result["data"][1]["message"],
                         "incident record has been created")

    def test_delete_incident(self):
        response = self.app.post('/api/v1/incidents')
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(result["data"][1]["message"],
                         "incident record has been deleted")

    def test_update_incident(self):
        response = self.app.post(
            'api/v1/incident', data=json.dumps(self.incident1),
            content_type='aplication/json')  # dumps convert data into json
        # content type notifies the data being sent os in json formart
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(result["data"][1]["message"],
                         "incident record has been updated")
