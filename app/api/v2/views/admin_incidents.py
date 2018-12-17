from flask_restful import Resource
from flask import request
from app.api.v2.validation.validation import ViewsValidation
from app.api.v2.models.incidents_model import IncidentsModel
from app.api.v2.models.users_model import UsersModel
from app.api.v2.auth_decorators.auth_decorator import isAdmin, isAuthenticated


class IncidentsAdmin(Resource):
    """
    resource to handle admin fuctionality
    :edit an incident status
    """
    @isAdmin
    @isAuthenticated
    def patch(self, incident_type, incident_id):
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
            incident_type, data, "status"
        )

        if valid_fields:
            # found missing fields
            return valid_fields

        try:
            # instanciate incident model incident type
            incident = IncidentsModel(
                incident_type=incident_type
            )

            update_incident = incident.update_incident(
                "incident_status", data["incident_status"], incident_id)

            if update_incident:
                # incident update success return incident data
                return {
                    "status": "success",
                    "message": "Updated {} status".format(incident_type),
                    "data": [
                        update_incident[0],
                    ]
                }, 200
            else:
                return ViewsValidation().views_error(
                    404, "Patch Failed, {}"
                    " Record Found".format(incident_type))

        except Exception as error:

            return ViewsValidation().views_error(
                403, "Failed to patch {} record  ::: {}"
                .format(incident_type, error))
