from app import create_app
import os
import json
from unittest import TestCase
from app.db.db_config import DbModel
from test_incidents_data import incident1, incident2, incident3, incident4,\
    incident5, comment_data, location_data, incident_no_media_intervention,\
    incident_no_media_redflag, incident2_invalid_field, comment_data_2, \
    location_data_2
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

    def add_incident(self, incident_type=None,
                     incident_data=None, registered=None):
        """
        method to add new incident
        registered: (boloean) decides to sign_in or sign_up
        in order to get auth token
        """

        # login to get token

        if registered:
            # user already registered sign in
            token = self.get_token("signin")

        else:
            # user not found register new user
            token = self.get_token("register")

        new_incident = self.app.post(
            "/api/v2/{}".format(incident_type), data=json.dumps(incident_data),
            headers={
                "Content-Type": "application/json",
                "Authorization": "Bearer "+token
            }
        )
        return new_incident

    def get_single_incident(self, incident_type, incident_id):
        """
        method query single incident, based on incident_id
        """
        token = self.get_token("signin")

        single_incident = self.app.get(
            "/api/v2/{}/{}".format(incident_type, incident_id),
            headers={
                "Content-Type": "application/json",
                "Authorization": "Bearer "+token
            }
        )
        return single_incident

    def get_all_incidents(self, incident_type):
        """
        method to add new incident, based on incident type
        """
        # login to get token
        token = self.get_token("signin")

        new_incident = self.app.get(
            "/api/v2/{}".format(incident_type),
            headers={
                "Content-Type": "application/json",
                "Authorization": "Bearer "+token
            }
        )
        return new_incident

    def get_token(self, auth_type="register"):

        if auth_type == "register":
            # user not found register new user
            register_response_data = json.loads(self.signup_user(
                sign_up_data
            ).data.decode())
        else:
            register_response_data = json.loads(self.signin_user(
                sign_in_data
            ).data.decode())

        token = register_response_data["data"][0]["token"]

        return token

    def delete_incident(self, incident_type, incident_id):
        """
        method to delete incident, based on incident_id
        """
        # login to get token
        token = self.get_token("signin")

        del_incident = self.app.delete(
            "/api/v2/{}/{}".format(incident_type, incident_id),
            headers={
                "Content-Type": "application/json",
                "Authorization": "Bearer "+token
            }
        )
        return del_incident

    def update_incident(self, incident_type, incident_id, field, update_data):
        """
        method to update incident, based on incident_id
        """
        # login to get token
        token = self.get_token("signin")

        patch_incident = self.app.patch(
            "/api/v2/{}/{}/{}".format(incident_type, incident_id, field),
            data=json.dumps(update_data),
            headers={
                "Content-Type": "application/json",
                "Authorization": "Bearer "+token
            }
        )
        return patch_incident

    def test_create_intervention(self):
        """
        method to test create incident endpoint
        incident_type: intervention
        """
        response = self.add_incident(
            "interventions", incident2)
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(
            result["data"][0]["message"],
            "created interventions record"
        )

    def test_create_intervention_bad_url(self):
        """ bad url test"""

        response = self.add_incident(
            "interventionz", incident2)
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 405)
        self.assertEqual(
            result["error"],
            "Invalid Endpoint interventionz "
        )

    def test_create_intervention_validation(self):
        """
        method to test create incident endpoint fields
        validation
        incident_type: intervention
        """
        response = self.add_incident(
            "interventions", incident2_invalid_field)
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            result["error"],
            "Invalid fields ['my_field', 'responder']"
        )

    def test_create_redflag(self):
        """
        method to test create incident endpoint
        incident_type: intervention
        """
        response = self.add_incident("redflags", incident1)
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(
            result["data"][0]["message"],
            "created redflags record"
        )

    def test_get_all_interventions(self):
        """
        method to test create incident endpoint
        incident_type: interventions
        """
        # add mock data to databse: 2 records
        self.add_incident("interventions", incident2)
        self.add_incident("interventions", incident4, True)

        # get all incidents

        response = self.get_all_incidents(
            "interventions")
        result = json.loads(response.data)

        # assert data: title, incident_type, comment
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            result["data"][0]["comment"],
            "ignore it or cover it up, out of sight out of mind"
        )
        self.assertEqual(
            result["data"][1]["comment"],
            "How many buildings should collapse for us to learn"
        )
        self.assertEqual(result["data"][0]["title"], "Manhole Hazard")
        self.assertEqual(
            result["data"][1]["title"],
            "Building Collpase Hazard"
        )
        self.assertEqual(result["data"][0]["incident_type"], "interventions")
        # should return 2 records
        self.assertEqual(len(result["data"]), 2)

    def test_get_all_redflags(self):
        """
        method to test create incident endpoint
        incident_type: redflags
        """
        # add mock data to databse 3 records
        self.add_incident("redflags", incident1)
        self.add_incident("redflags", incident3, True)
        self.add_incident("redflags", incident5, True)

        # get all red flags 2 records should be returned
        response = self.get_all_incidents("redflags")
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            result["data"][0]["comment"],
            "This is all fake news i tell ya"
        )
        self.assertEqual(
            result["data"][2]["comment"],
            "This is some next level tribalism"
        )
        self.assertEqual(result["data"][0]["title"], "Traffic Corruption")
        self.assertEqual(result["data"][0]["incident_type"], "redflags")
        # should return two records
        self.assertEqual(len(result["data"]), 3)

    def test_delete_redflag(self):
        """
        method to test redflag deletion
        incident_type: redflags
        """
        # add mock data to databse: 2 records
        res_red_flag_a = self.add_incident("redflags", incident1)
        res_red_flag_b = self.add_incident("redflags", incident3, True)

        # retrieve data (incident_id) from inserted records
        res_red_flag_a = json.loads(res_red_flag_a.data)
        res_red_flag_b = json.loads(res_red_flag_b.data)

        incident_id_a = res_red_flag_a["data"][0]["id"]
        incident_id_b = res_red_flag_b["data"][0]["id"]

        # delete red flags  by id
        response = self.delete_incident(
            "redflags", incident_id_a
        )
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            result["message"],
            "Deleted redflags record"
        )
        self.assertEqual(
            result["data"][0]["incident_id"],
            incident_id_a
        )

        # query redflags only one should be left
        result_get_all = self.get_all_incidents("redflags")
        response_get_all = json.loads(result_get_all.data)

        self.assertEqual(len(response_get_all["data"]), 1)

        response_b = self.delete_incident(
            "redflags", "klk"
        )
        result_b = json.loads(response_b.data)
        # invalid endpoint ID
        self.assertEqual(
            result_b["error"],
            "ID must be an Integer"
        )

    def test_delete_intervention(self):
        """
        method to test intervention deletion
        incident_type: interventions
        """
        # add mock data to databse: 2 records
        res_intv_a = self.add_incident("interventions", incident1)
        res_intv_b = self.add_incident("interventions", incident3, True)

        # retrieve data (incident_id) from inserted records
        res_intv_a = json.loads(res_intv_a.data)
        res_intv_b = json.loads(res_intv_b.data)

        incident_id_a = res_intv_a["data"][0]["id"]
        incident_id_b = res_intv_b["data"][0]["id"]

        # delete red flags  by id
        response = self.delete_incident(
            "interventions", incident_id_a
        )
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            result["message"],
            "Deleted interventions record"
        )
        self.assertEqual(
            result["data"][0]["incident_id"],
            incident_id_a
        )

        # query interventions only one should be left
        result_get_all = self.get_all_incidents("interventions")
        response_get_all = json.loads(result_get_all.data)

        self.assertEqual(len(response_get_all["data"]), 1)

    def test_get_single_redflag(self):
        """
        method to test single redflag
        incident_type: redflag
        """
        # add mock data to databse: 2 redflag records
        res_redflag_a = self.add_incident("redflags", incident1)
        res_redflag_b = self.add_incident("redflags", incident3, True)

        result_b = json.loads(res_redflag_a.data)
        incident_id = result_b["data"][0]["id"]

        response = self.get_single_incident(
            "redflags",
            incident_id
        )
        result = json.loads(response.data)
        # assert red flag title
        self.assertEqual(result["data"][0]["title"], "Traffic Corruption")
        # assert single record returned
        self.assertEqual(len(result["data"]), 1)
        # assert returned incident_id
        self.assertEqual(incident_id, result["data"][0]["incident_id"])

    def test_update_redflag_comment(self):
        """
        method to test update redflag comment
        incident_type: redflag
        """
        # add mock data to databse: 2 redflag records
        res_redflag_a = self.add_incident("redflags", incident1)
        res_redflag_b = self.add_incident("redflags", incident3, True)

        result_b = json.loads(res_redflag_b.data)
        incident_id = result_b["data"][0]["id"]

        response = self.update_incident(
            "redflags",
            incident_id,
            "comment",
            comment_data,
        )
        result = json.loads(response.data)
        print("RESULT!!", result)
        # assert updated redflag comment
        self.assertEqual(result["data"][0]["comment"], comment_data["comment"])
        # assert success message
        self.assertEqual(result["message"], "Updated redflags comment")
        # assert returned incident_id
        self.assertEqual(incident_id, result["data"][0]["incident_id"])

    def test_update_redflag_location(self):
        """
        method to test update redflag comment
        incident_type: redflag
        """
        # add mock data to databse: 2 redflag records
        res_redflag_a = self.add_incident("redflags", incident1)
        res_redflag_b = self.add_incident("redflags", incident3, True)

        result_b = json.loads(res_redflag_b.data)
        incident_id = result_b["data"][0]["id"]

        response = self.update_incident(
            "redflags",
            incident_id,
            "location",
            location_data,
        )
        result = json.loads(response.data)
        print("Location", result)

        # assert updated redflag lcation
        self.assertEqual(
            result["data"][0]["location"],
            location_data["location"]
        )
        # assert redflag comment remain unchanged
        self.assertEqual(
            result["data"][0]["comment"],
            "This is some next level nepotism"
        )
        # assert success message
        self.assertEqual(result["message"], "Updated redflags location")
        # assert returned incident_id
        self.assertEqual(incident_id, result["data"][0]["incident_id"])

    def tearDown(self):
        """empty table data after each test"""
        self.db.truncate_tables()
