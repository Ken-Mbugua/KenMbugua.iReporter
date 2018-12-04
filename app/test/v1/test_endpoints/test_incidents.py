import os
from unittest import TestCase
import json

from app import create_app

app = create_app("testing")


class TestIncidents(TestCase):
    def setUp(self):
        self.app = app.test_client()
        # app.testing = True
        self.app_context = app.app_context()
        self.app_context.push()

        # test data
        self.incident1 = {
            'title': 'Traffice Corruption',
            'description': 'Offices taking bribes',
            'type': 'RedFlag',
            'status': 'Rejected',
            'location': '-34444400, 3444499900',
            'image': [
                {
                      'dir': 'var/www/uploads/incidents/img/USR-232455.jpeg',
                      'filesize': '2045kb'
                },
                {
                    'dir': 'var/www/uploads/incidents/img/USR-232455.jpeg',
                    'filesize': '2045kb'
                }
            ],
            'video': [
                {
                    'dir': 'var/www/uploads/readflags/video/USR-232455.mp4',
                    'filesize': '340098245Kb'
                }, {
                    'dir': 'var/www/uploads/readflags/video/USR-232455.mp4',
                    'filesize': '340098245Kb'
                }
            ],
            'comment': 'This is fake all news i tell ya'


        }
        # test data

        self.incident2 = {
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
            "comment": "This is fake all news i tell ya"
        }

        self.comment_data = {
            "comment": "Scintilating"
        }
        self.location_data = {
            "location": "-3455666, 42254555"
        }

    def add_incident(self):
        """
        method to add new incident
        """
        new_incident = self.app.post(
            "/api/v1/incidents", data=json.dumps(self.incident2),
            headers={"Content-Type": "application/json"})
        return new_incident

    def test_get_all_inicidents(self):
        """
        method to test GET all incident endpoint
        """
        response = self.app.get("/api/v1/incidents")
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(result["status"], 200)

    def test_create_incident(self):
        """
        method to test Create incident endpoint
        """
        response = self.app.post(
            "/api/v1/incidents", data=json.dumps(self.incident1),
            headers={"Content-Type": "application/json"})
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(result["data"][0]["message"],
                         "incident record has been created")

    def test_delete_incident(self):
        """
        method to test DELETE incident endpoint
        """
        response = self.app.delete(
            '/api/v1/incidents/1')  # record created by test_create_incident
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        # print("JSON_BUMPZ::", result["data"])
        self.assertEqual(result["data"][0]["message"],
                         "incident record has been deleted")

    def test_delete_incident_not_found(self):
        # any index above 1 == index not found
        response = self.app.delete('/api/v1/incidents/28')
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(result["error"],
                         "Not found for id 28")

    def test_update_incident_location(self):
        """
        method to test UPDATE incident endpoint
        """
        self.add_incident()

        response = self.app.patch(
            # dumps converts data into json
            "api/v1/incidents/1/location", data=json.dumps(self.incident1),
            headers={"Content-Type": "application/json"})
        # content type notifies the data being sent is in json formart
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(result["data"][0]["message"],
                         "incident record has been updated")

    def test_update_incident_location_not_found(self):
        """
        method to test UPDATE incident endpoint
        """
        self.add_incident()

        response = self.app.patch(
            # dumps converts data into json
            "api/v1/incidents/32/location", data=json.dumps(self.incident1),
            headers={"Content-Type": "application/json"})
        # content type notifies the data being sent is in json formart
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(result["error"],
                         "Not found for id 32")

    def test_update_incident_comment(self):
        """
        method to test UPDATE incident endpoint
        """
        self.add_incident()

        response = self.app.patch(
            # dumps converts data into json
            "api/v1/incidents/1/comment", data=json.dumps(self.incident1),
            headers={"Content-Type": "application/json"})
        # content type notifies the data being sent is in json formart
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(result["data"][0]["message"],
                         "incident record has been updated")

    def test_update_incident_comment_not_found(self):
        """
        method to test UPDATE comment incident endpoint
        """
        self.add_incident()

        response = self.app.patch(
            # dumps converts data into json
            "api/v1/incidents/32/comment", data=json.dumps(self.incident1),
            headers={"Content-Type": "application/json"})
        # content type notifies the data being sent is in json formart
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(result["error"],
                         "Not found for id 32")

    def test_update_incident(self):
        """
        method to test UPDATE incident endpoint
        """
        self.add_incident()

        response = self.app.patch(
            # dumps converts data into json
            "api/v1/incidents/1/comment", data=json.dumps(self.incident1),
            headers={"Content-Type": "application/json"})
        # content type notifies the data being sent is in json formart
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(result["data"][0]["message"],
                         "incident record has been updated")

    def test_update_incident_not_found(self):
        """
        method to test UPDATE incident endpoint
        """
        self.add_incident()

        response = self.app.patch(
            # dumps converts data into json
            "api/v1/incidents/32/comment", data=json.dumps(self.incident1),
            headers={"Content-Type": "application/json"})
        # content type notifies the data being sent is in json formart
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(result["error"],
                         "Not found for id 32")

        # index not found

    # def test_get_all_inicidents_invalid_url(self):
    #     """
    #     method to test GET all incident endpoint
    #     """
    #     response = self.app.get("/api/v1/incidentsz")
    #     result = json.loads(response.data)
    #     self.assertEqual(response.status_code, 404)
    #     # self.assertEqual(result["status"], 200)
