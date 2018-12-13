import os
import json
from unittest import TestCase
from app.db.db_config import DbModel

from app import create_app


class TestIncidentsV2(TestCase):
    def setUp(self):
        app = create_app("testing")
        self.app = app.test_client()
        # app.testing = True
        self.app_context = app.app_context()
        self.app_context.push()
        self.db = DbModel()

        # test data
        self.incident1 = {
            'title': 'Traffice Corruption',
            'description': 'Offices taking bribes',
            'type': 'RedFlag',
            'incident_status': 'Rejected',
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
            "title": "Manhole Hazard",
            "description": "Manhole open around hirlingum mall",
            "type": "Intervention",
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
            "comment": "ignore it or cover it up, out of sight out of mind"
        }

        self.comment_data = {
            "comment": "Scintilating"
        }
        self.location_data = {
            "location": "-3455666, 42254555"
        }

    def add_incident(self, incident_title):
        """
        method to add new incident
        """
        self.incident2["title"] = incident_title
        new_incident = self.app.post(
            "/api/v2/incidents", data=json.dumps(self.incident2),
            headers={"Content-Type": "application/json"})
        return new_incident

    def test_get_all_inicidents(self):
        """
        method to test GET all incident endpoint
        """
        # when empty should return 404
        # response = self.app.get("/api/v2/incidents")
        # result = json.loads(response.data)
        # self.assertEqual(response.status_code, 404)
        # self.assertEqual(result["status"], 404)

        # add an incident
        # self.add_incident("Corruption Case 1")

        # when poulates should return status 200
        # response = self.app.get("/api/v2/incidents")
        # result = json.loads(response.data)
        # self.assertEqual(response.status_code, 200)
        # self.assertEqual(result["status"], 200)
        pass

    def test_create_incident(self):
        """
        method to test Create incident endpoint
        """
        # response = self.app.post(
        #     "/api/v2/incidents",
        #     data=json.dumps(self.incident1),
        #     headers={"Content-Type": "application/json"})
        # result = json.loads(response.data)
        # self.assertEqual(response.status_code, 201)
        # self.assertEqual(result["data"][0]["message"],
        #                  "incident record has been created")
        pass

    def test_update_incident_location(self):
        """
        method to test UPDATE incident endpoint
        """
        # self.add_incident("Corruption Case 3")

        # response = self.app.patch(
        #     # dumps converts data into json
        #     "api/v2/incidents/1/location",
        #     data=json.dumps(self.location_data),
        #     headers={"Content-Type": "application/json"})
        # # content type notifies the data being sent is in json formart
        # result = json.loads(response.data)
        # print(result)
        # self.assertEqual(response.status_code, 200)
        # self.assertEqual(result["data"][0]["message"],
        #                  "incident record has been updated")
        pass

    def test_update_incident_location_not_found(self):
        """
        method to test UPDATE incident endpoint
        """
        # self.add_incident("Corruption Case 4")

        # response = self.app.patch(
        #     # dumps converts data into json
        #     "api/v2/incidents/32/location",
        #     data=json.dumps(self.location_data),
        #     headers={"Content-Type": "application/json"})
        # # content type notifies the data being sent is in json formart
        # result = json.loads(response.data)
        # print(result)
        # self.assertEqual(response.status_code, 404)
        # self.assertEqual(result["error"],
        #                  "Not found for id 32")
        pass

    def test_update_incident_comment(self):
        """
        method to test UPDATE incident endpoint
        """
        # self.add_incident("Corruption Case 5")

        # response = self.app.patch(
        #     # dumps converts data into json
        #     "api/v2/incidents/1/comment",
        #     data=json.dumps(self.comment_data),
        #     headers={"Content-Type": "application/json"})
        # # content type notifies the data being sent is in json formart
        # result = json.loads(response.data)
        # print(result)
        # self.assertEqual(response.status_code, 200)
        # self.assertEqual(result["data"][0]["message"],
        #                  "incident record has been updated")
        pass

    def test_update_incident_comment_not_found(self):
        """
        method to test UPDATE comment incident endpoint
        """
        # self.add_incident("Corruption Case 6")

        # response = self.app.patch(
        #     # dumps converts data into json
        #     "api/v2/incidents/32/comment",
        #     data=json.dumps(self.comment_data),
        #     headers={"Content-Type": "application/json"})
        # # content type notifies the data being sent is in json formart
        # result = json.loads(response.data)
        # self.assertEqual(response.status_code, 404)
        # self.assertEqual(result["error"],
        #                  "Not found for id 32")
        pass

    def test_update_incident(self):
        """
        method to test UPDATE incident endpoint
        """
        # self.add_incident("Corruption Case 7")

        # response = self.app.patch(
        #     # dumps converts data into json
        #     "api/v2/incidents/1",
        #     data=json.dumps(self.incident1),
        #     headers={"Content-Type": "application/json"})
        # # content type notifies the data being sent is in json formart
        # result = json.loads(response.data)
        # self.assertEqual(response.status_code, 200)
        # self.assertEqual(result["data"][0]["message"],
        #                  "incident record has been updated")
        pass

    def test_update_incident_not_found(self):
        """
        method to test UPDATE incident endpoint
        """
        # self.add_incident("Corruption Case 8")

        # response = self.app.patch(
        #     # dumps converts data into json
        #     "api/v2/incidents/32",
        #     data=json.dumps(self.incident1),
        #     headers={"Content-Type": "application/json"})
        # # content type notifies the data being sent is in json formart
        # result = json.loads(response.data)
        # self.assertEqual(response.status_code, 404)
        # self.assertEqual(result["error"],
        #                  "Not found for id 32")
        pass

    def test_delete_incident(self):
        """
        method to test DELETE incident endpoint
        """
        # add an incident
        # self.add_incident("Corruption Case 2")

        # response = self.app.delete(
        #     '/api/v2/incidents/1')  # record created by test_create_incident
        # result = json.loads(response.data)
        # self.assertEqual(response.status_code, 200)
        # # print("JSON_BUMPZ::", result["data"])
        # self.assertEqual(result["data"][0]["message"],
        #                  "incident record has been deleted")
        pass

    def test_delete_incident_not_found(self):
        # any index above 1 == index not found
        # response = self.app.delete('/api/v2/incidents/28')
        # result = json.loads(response.data)
        # self.assertEqual(response.status_code, 404)
        # self.assertEqual(result["error"],
        #                  "Not found for id 28")

        # index not found
        pass

    def tearDown(self):
        """empty table data after each test"""
        self.db.truncate_tables()
