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
            return ViewValidation().views_error(
                400, "Bad Request Format")

        if ViewsValidation().check_fields(incident_type, data):
            # found missing fields
            return ViewsValidation().check_fields(fields, data)

        # instanciate incident model and pass incident data
        incident = IncidentsModel(**data)

        response = incident.create_incident()

        if response:
            incident_details = incident.get_last_incident()
            return {  # incident creation success return incident data
                "status": 201,
                "data": [{
                    "id": incident_details[0],
                    "message": "created {} record"
                    .format(incident.incident_type)
                }]
            }, 201
