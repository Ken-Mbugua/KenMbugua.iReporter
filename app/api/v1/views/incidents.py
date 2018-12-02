from flask_restful import Resource
from flask import request
from app.api.v1.models.incidents_model import IncidentsModel


class Incidents(Resource, IncidentsModel):
    def __init__(self):
        self.incident = IncidentsModel()

    def post(self):
        """
        method to receive incident data and pass to db model save()
        """
        data = request.get_json()
        incident_entry = {
            "title": data["title"],
            "description": data["description"],
            "status": data["status"],
            "location": data["location"],
            "type": data["type"],
            "image": data["image"],
            "video": data["video"],
            "comment": data["comment"],
            "createdBy": 34
        }

        res = self.incident.save(incident_entry)
        if res:
            return {
                "status": 201,
                "data": [{
                    "id": res["id"],
                    "message": "red-flag record has been created"
                }]
            }, 201

        else:
            return {
                "status": 400,
                "error": "Bad Request"
            }, 400

    def get(self):
        """
        method to query all incidences from db
        """
        return {
            "status": 200,
            "data": self.incident.get_incidents()
        }, 200


class IncidentsId(Resource, IncidentsModel):
    def __init__(self):
        self.db = IncidentsModel()

    def get(self, incident_id):
        """
        method to handle GET single incident request
        """
        res = self.db.get_incident(incident_id)

        if res:
            return {
                "status": 200,
                "data": [res]
            }, 200
        else:
            return {
                "status": 404,
                "error": "incident with id {} "
                "was not found ".format(incident_id)
            }, 404
