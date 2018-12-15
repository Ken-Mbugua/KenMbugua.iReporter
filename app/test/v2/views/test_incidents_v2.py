from app import create_app
import os
import json
from unittest import TestCase
from app.db.db_config import DbModel
from test_incidents_data import incident1, incident2, comment_data,\
    location_data, incident_no_media_intervention, incident_no_media_redflag
from test_data_auth import sign_in_data, sign_up_data


class TestIncidentsV2(TestCase):
    def setUp(self):
        app = create_app("testing")
        self.app = app.test_client()
        # app.testing = True
        self.app_context = app.app_context()
        self.app_context.push()
        self.db = DbModel()

    def signin_user(self, user_data):
        """
        method for mock signin
        purpose: to get token
        """
        response = self.app.post(
            'api/v2/auth/login',
            data=json.dumps(user_data),
            headers={
                "Content-Type": "application/json"
            }
        )

        return response

    def signup_user(self, user_data):
        """
        method for mock signup
        purpose: to get token
        """
        response = self.app.post(
            'api/v2/auth/signup',
            data=json.dumps(user_data),
            headers={
                "Content-Type": "application/json"
            }
        )

        return response

    def add_incident(self, incident_type, incident_data):
        """
        method to add new incident
        """

        # login to get token
        register_response_data = json.loads(self.signup_user(
            sign_up_data
        ).data.decode())

        token = register_response_data["data"][0]["token"]

        new_incident = self.app.post(
            "/api/v2/{}".format(incident_type), data=json.dumps(incident_data),
            headers={
                "Content-Type": "application/json",
                "Authorization": "Bearer "+token
            }
        )
        return new_incident

    def test_create_redflag(self):
        """
        method to test create incident endpoint
        incident_type: intervention
        """
        response = self.add_incident(
            "interventions", incident_no_media_intervention)
        result = json.loads(response.data)
        print("RESULT::", result)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(result["data"][0]["message"],
                         "created Intervention record")

    def test_create_incident(self):
        """
        method to test create incident endpoint
        incident_type: intervention
        """
        response = self.add_incident("redflags", incident_no_media_redflag)
        result = json.loads(response.data)
        print("RESULT::", result)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(result["data"][0]["message"],
                         "created RedFlag record")

    def tearDown(self):
        """empty table data after each test"""
        self.db.truncate_tables()
