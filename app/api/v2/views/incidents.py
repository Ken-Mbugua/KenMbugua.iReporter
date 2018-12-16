from flask_restful import Resource
from flask import request
from app.api.v2.validation.validation import ViewsValidation
from app.api.v2.models.incidents_model import IncidentsModel
from app.api.v2.models.users_model import UsersModel
from app.api.v2.auth_decorators.auth_decorator import isAdmin, isAuthenticated


class Incidents(Resource):

    @isAuthenticated
    def post(self, incident_type):
        """
        method to receive incident data and pass to db model save()
        """
        if incident_type not in ["redflags", "interventions"]:
            return ViewsValidation().views_error(
                405, "Invalid Endpoint {} ".format(incident_type))

        data = request.get_json(silent=True)
        # validate received fileds
        if not data:
            return ViewsValidation().views_error(
                400, "Bad Request Format")

        valid_fields = ViewsValidation().check_fields(incident_type, data)
        if valid_fields:
            # found missing fields
            return valid_fields

        try:
            # decode token to obtain email then user_id
            auth_header = request.headers.get('Authorization')
            if auth_header:
                auth_token = auth_header.split(" ")[1]
                user_email = UsersModel().decode_auth_token(
                    auth_token)["email"]

                user_id = UsersModel().get_user_by_email(user_email)[0]

                # instanciate incident model and pass incident data
                incident = IncidentsModel(**data, created_by=user_id,
                                          incident_type=incident_type)

                # insert incident in db
                incident.create_incident()
            else:
                ViewsValidation().views_error(
                    401, "Provide a valid token", "error")

            incident_details = incident.get_last_incident()
            return {  # incident creation success return incident data
                "status": 201,
                "data": [{
                      # return incident_id at index 0
                      "id": incident_details[0],
                      "message": "created {} record"
                    .format(incident.incident_type)
                }]
            }, 201
        except Exception as error:

            return ViewsValidation().views_error(
                403, "Failed To create {}:::\n {}"
                .format(incident_type, error))

    @isAuthenticated
    def get(self, incident_type):
        """
        method to query all incident data from database
        """
        if incident_type not in ["redflags", "interventions"]:
            return ViewsValidation().views_error(
                405, "Invalid Endpoint {}".format(incident_type))
        try:
            # instanciate incident model incident type
            incident = IncidentsModel(
                incident_type=incident_type
            )

            all_incidents = incident.get_incident_by(
                "incident_type", incident_type)
            if all_incidents:
                return {  # incident creation success return incident data
                    "status": 200,
                    "data":
                        # return all incidents
                        all_incidents
                }, 200
            else:
                return ViewsValidation().views_error(
                    404, "No {} records found".format(incident_type))

        except Exception as error:

            return ViewsValidation().views_error(
                403, "Failed to query all {}:::\n {}"
                .format(incident_type, error))


class IncidentsID(Resource):
    """class to operate on incidents based on incident id"""

    @isAuthenticated
    def get(self, incident_type, incident_id):
        """
        method to get an incident from database
        """

        if incident_type not in ["redflags", "interventions"]:
            return ViewsValidation().views_error(
                405, "Invalid Endpoint {} ".format(incident_type)
            )

        if ViewsValidation().validate_id(incident_id):
            return ViewsValidation().validate_id(incident_id)

        try:
            # instanciate incident model incident type
            incident = IncidentsModel(
                incident_type=incident_type
            )

            one_incident = incident.get_incident_by(
                "incident_id", incident_id)
            if one_incident:
                # incident query success return incident data
                return {
                    "status": 200,
                    "data":
                        one_incident
                }, 200
            else:
                return ViewsValidation().views_error(
                    404, "No {} record found".format(incident_type))

        except Exception as error:

            return ViewsValidation().views_error(
                403, "Failed to get {} record  ::: {}"
                .format(incident_type, error))

    @isAuthenticated
    def delete(self, incident_type, incident_id):
        """
        method to delete an incident from database
        """

        if incident_type not in ["redflags", "interventions"]:
            return ViewsValidation().views_error(
                405, "Invalid Endpoint {} ".format(incident_type)
            )

        if ViewsValidation().validate_id(incident_id):
            return ViewsValidation().validate_id(incident_id)

        try:
            # instanciate incident model incident type
            incident = IncidentsModel(
                incident_type=incident_type
            )

            del_incidents = incident.delete_incident(
                "incident_id", incident_id)
            if del_incidents:
                # incident deletion success return incident id and message
                return {
                    "status": 200,
                    "data": [{
                        "id": del_incidents[0]["incident_id"],
                        "message": "Deleted {} record".format(incident_type)
                    }]
                }, 200
            else:
                return ViewsValidation().views_error(
                    404, "No {} record found".format(incident_type))

        except Exception as error:

            return ViewsValidation().views_error(
                403, "Failed to delete {} record  ::: {}"
                .format(incident_type, error))


class IncidentsPatch(Resource):

    @isAuthenticated
    def patch(self, incident_type, incident_id, field):
        """
        method to update an incident by field provided
        """

        if incident_type not in ["redflags", "interventions"]:
            return ViewsValidation().views_error(
                405, "Invalid Endpoint {} ".format(incident_type)
            )

        if ViewsValidation().validate_id(incident_id):
            return ViewsValidation().validate_id(incident_id)

        data = request.get_json(silent=True)
        # validate received fileds
        if not data:
            return ViewsValidation().views_error(
                400, "Bad Request Format")

        valid_fields = ViewsValidation().check_fields(
            incident_type, data, field
        )

        if valid_fields:
            # found missing fields
            return valid_fields

        try:
            # instanciate incident model incident type
            incident = IncidentsModel(
                incident_type=incident_type
            )

            # update_incident(self, field, field_data, incident_id)

            update_incident = incident.update_incident(
                field, data[field], incident_id)

            if update_incident:
                # incident update success return incident data
                return {
                    "status": 200,
                    "data": [{
                        "id": update_incident[0]["incident_id"],
                        "message": "Updated {} record ".format(incident_type)
                    }]
                }, 200
            else:
                return ViewsValidation().views_error(
                    404, "Pach Failed, No {}"
                    " record found".format(incident_type))

        except Exception as error:

            return ViewsValidation().views_error(
                403, "Failed to patch {} record  ::: {}"
                .format(incident_type, error))
