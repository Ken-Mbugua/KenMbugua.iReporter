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
                405, "Invalid Endpoint {} ".format(incident_type)
            )

        data = request.get_json(silent=True)
        # validate received fileds
        if not data:
            return ViewsValidation().views_error(
                400, "Bad Request Format")

        valid_fields = ViewsValidation().check_fields(incident_type, data)
        if valid_fields:
            # found missing fields
            return valid_fields

        # validate all fields
        valid_field_data = ViewsValidation().check_fields_data(data)
        if valid_field_data:
            # found invalid data in fields
            return valid_field_data

        try:
            # decode token to obtain email then user_id
            auth_header = request.headers.get('Authorization')
            if auth_header:
                auth_token = auth_header.split(" ")[1]
                user_email = UsersModel().decode_auth_token(
                    auth_token)["email"]

                user_id = UsersModel().get_user_by_email(user_email)[0]

                # instanciate incident model and pass incident data
                incident = IncidentsModel(
                    **data,
                    created_by=user_id,
                    incident_type=incident_type
                )

                # insert incident in db
                incident.create_incident()
            else:
                ViewsValidation().views_error(
                    401, "Provide a valid token", "error"
                )

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
            # get user details from auth token
            auth_token_data = UsersModel().get_user_details_from_token(request)

            if auth_token_data:
                user_id = auth_token_data["user_id"]
                role = auth_token_data["role"]

            # instanciate incident model incident type
            incident = IncidentsModel(
                incident_type=incident_type,
                created_by=user_id
            )

            all_incidents = incident.get_incident_by(
                "incident_type", incident_type, role)
            if all_incidents:
                return {  # incident creation success return incident data
                    "status": 200,
                    "data":
                        # return all incidents
                        all_incidents
                }, 200
            else:
                return ViewsValidation().views_error(
                    404, "Fetch Failed, {} "
                    "Records not Found".format(incident_type))

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

        endpoint_validate = ViewsValidation().validate_endpoint(
            incident_type, incident_id)

        if endpoint_validate:
            return endpoint_validate

        try:
            # get user details from auth token
            auth_token_data = UsersModel().get_user_details_from_token(request)

            if auth_token_data:
                user_id = auth_token_data["user_id"]

            # instanciate incident model incident type
            incident = IncidentsModel(
                incident_type=incident_type,
                created_by=user_id
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
                    404, "Fetch Failed, {} "
                    "Record not Found".format(incident_type))

        except Exception as error:

            return ViewsValidation().views_error(
                403, "Failed to get {} record  ::: {}"
                .format(incident_type, error))

    @isAuthenticated
    def delete(self, incident_type, incident_id):
        """
        method to delete an incident from database
        """

        endpoint_validate = ViewsValidation().validate_endpoint(
            incident_type, incident_id)

        if endpoint_validate:
            return endpoint_validate

        try:
            # get user details from auth token
            auth_token_data = UsersModel().get_user_details_from_token(request)

            if auth_token_data:
                user_id = auth_token_data["user_id"]

            # instanciate incident model incident type
            incident = IncidentsModel(
                incident_type=incident_type,
                created_by=user_id
            )
            can_delete = incident.can_update_or_delete(incident_id)
            if not can_delete:
                return ViewsValidation().views_error(
                    403, "Deletion Failed, Record is no Longer Drafted"
                )

            del_incidents = incident.delete_incident(
                "incident_id", incident_id)

            if del_incidents:
                # incident deletion success return incident id and message
                return {
                    "status": "success",
                    "message": "Deleted {} record".format(incident_type),
                    "data": [
                        del_incidents[0]
                    ]
                }, 200
            else:
                return ViewsValidation().views_error(
                    404, "Deletion Failed, {} "
                    "Record not Found".format(incident_type))

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
        endpoint_validate = ViewsValidation().validate_endpoint(
            incident_type, incident_id, field)

        if endpoint_validate:
            return endpoint_validate

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

        # validate all fields
        valid_field_data = ViewsValidation().check_fields_data(data)
        if valid_field_data:
            # found invalid data in fields
            return valid_field_data

        try:
            # get user details from auth token
            auth_token_data = UsersModel().get_user_details_from_token(request)

            if auth_token_data:
                user_id = auth_token_data["user_id"]
                role = auth_token_data["role"]

            # instanciate incident model incident type
            incident = IncidentsModel(
                incident_type=incident_type,
                created_by=user_id
            )

            # update_incident(self, field, field_data, incident_id)
            can_update = incident.can_update_or_delete(incident_id)
            if not can_update:
                return ViewsValidation().views_error(
                    403, "Patch Failed,"
                    " Record is no Longer Drafted".format(incident_type))

            update_incident = incident.update_incident(
                field, data[field], incident_id, role
            )

            if update_incident:
                # incident update success return incident data
                return {
                    "status": "success",
                    "message": "Updated {} {}".format(incident_type, field),
                    "data": [
                        update_incident[0],
                    ]
                }, 200
            else:
                return ViewsValidation().views_error(
                    404, "Patch Failed, {} "
                    " Record not Found".format(incident_type))

        except Exception as error:

            return ViewsValidation().views_error(
                403, "Failed to patch {} record  ::: {}"
                .format(incident_type, error))
