from flask_restful import Resource
from flask import request
from app.api.v1.models.incidents_model import IncidentsModel


class IncidentsUpdateLocation(Resource, IncidentsModel):

    def patch(self, incident_id):
        """
        method to handle PATCH location request
        """
        data = request.get_json()

        # script to allow only location request.body
        key_list = [*data]
        if (len(key_list) == 1 and key_list[0] == "location"):

            new_incident_instance = IncidentsModel()
            res = new_incident_instance.edit_incident(incident_id, data)

            if res:
                return {
                    "status": 200,
                    "data": [{
                        "id": res["id"],
                        "message": "incident record has been updated"
                    }]
                }, 200
            else:
                return {
                    "status": 404,
                    "error": "Not found for id {}".format(incident_id)
                }, 404
        else:
            return {
                "status": 403,
                "error": "Bad Request only location is allowed"
            }, 403


class IncidentsUpdateComment(Resource, IncidentsModel):

    def patch(self, incident_id):
        """
        method to handle PATCH comment request
        """
        data = request.get_json()

        # script to allow only comment request.body
        key_list = [*data]
        if (len(key_list) == 1 and key_list[0] == "comment"):

            new_incident_instance = IncidentsModel()
            res = new_incident_instance.edit_incident(incident_id, data)

            if res:
                return {
                    "status": 200,
                    "data": [{
                        "id": res["id"],
                        "message": "incident record has been updated"
                    }]
                }, 200
            else:
                return {
                    "status": 404,
                    "error": "Not found for id {}".format(incident_id)
                }, 404
        else:
            return {
                "status": 403,
                "error": "Bad Request only comment is allowed"
            }, 403
