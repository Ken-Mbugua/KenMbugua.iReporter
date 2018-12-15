from flask_restful import Resource
from flask import request
from app.api.v2.validation.validation import ViewsValidation
from app.api.v2.models.incidents_model import IncidentsModel


class Incidents(Resource):

    def post(self, incident_type):
        """
        method to receive incident data and pass to db model save()
        """
        data = request.get_json(silent=True)
        # validate received fileds
        if not data:
            return ViewsValidation().views_error(
                400, "Bad Request Format")

        valid_fields = ViewsValidation().check_fields(incident_type, data)
        if valid_fields:
            # found missing fields
            return valid_fields

        # instanciate incident model and pass incident data
        incident = IncidentsModel(**data)

        try:
            incident.create_incident()

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
                403, "Failed To create {}:::{}"
                .format(incident.incident_type, error))
