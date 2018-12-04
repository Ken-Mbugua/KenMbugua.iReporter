from flask_restful import Resource
from flask import request
from app.api.v1.models.incidents_model import IncidentsModel


class Incidents(Resource, IncidentsModel):
    def __init__(self):
        self.incident = IncidentsModel()

    def post(self):
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
