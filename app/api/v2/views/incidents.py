from flask_restful import Resource
import datetime
from flask import request
from app.api.v2.validation.validation import ViewsValidation
from app.api.v2.models.incidents_model import IncidentsModel


class Incidents(Resource):
    def __init__(self):
        pass

    def post(self):
        """
        method to receive incident data and pass to db model save()
        """
        data = request.get_json(silent=True)
        # validate received fileds
        if not data:
            return ViewsValidation().views_error(
                400, "Bad Request Format")

        fields = [
            'title',
            'description',
            'incident_status',
            'comment',
            'video',
            'image',
            'location'
        ]

        if ViewsValidation().check_fields(fields, data):
            # found missing fields
            return ViewsValidation().check_fields(fields, data)

        # instanciate Users model and pass request data
        incidents = IncidentsModel(**data)

        #     res = self.incident.save(incident_entry)
        #     if res:
        #         if res["status"] == 400:
        #             return res, 400
        #         else:
        #             return {
        #                 "status": 201,
        #                 "data": [{
        #                     "id": res["id"],
        #                     "message": "incident record has been created"
        #                 }]
        #             }, 201

        #     else:
        #         return {
        #             "status": 400,
        #             "error": "Bad Request"
        #         }, 400
        # else:
        #     return {
        #         "status": 403,
        #         "error": "Bad request: missing"
        #         " fileds {}".format(missing_fields)
        #     }, 403

    def get(self):
        """
        method to query all incidences from db
        """
        res = self.incident.get_incidents()
        if res:
            return {
                "status": 200,
                "data": res
            }, 200
        else:
            return {
                "status": 404,
                "error": "No incidents found"
            }, 404


# class IncidentsId(Resource, IncidentsModel):
#     def __init__(self):
#         self.db = IncidentsModel()

#     def get(self, incident_id):
#         """
#         method to handle GET single incident request
#         """
#         res = self.db.get_incident_by_id(incident_id)

#         if res:
#             return {
#                 "status": 200,
#                 "data": [res]
#             }, 200
#         else:
#             return {
#                 "status": 404,
#                 "error": "incident with id {} "
#                 "was not found ".format(incident_id)
#             }, 404

#     def delete(self, incident_id):
#         """
#         method to handle DELETE single incident request
#         """
#         res = self.db.delete_incident(incident_id)

#         if res:
#             return {
#                 "status": 200,
#                 "data": [{
#                     "id": res["id"],
#                     "message": "incident record has been deleted"
#                 }]
#             }, 200
#         else:
#             return {
#                 "status": 404,
#                 "error": "Not found for id {}".format(incident_id)
#             }, 404

#     def patch(self, incident_id):
#         """
#         method to handle PATCH sigle incident request
#         any field provided can be updated here
#         """

#         data = request.get_json()

#         res = self.db.edit_incident(incident_id, data)

#         if res:
#             return {
#                 "status": 200,
#                 "data": [{
#                     "id": res["id"],
#                     "message": "incident record has been updated"
#                 }]
#             }, 200
#         else:
#             return {
#                 "status": 404,
#                 "error": "Not found for id {}".format(incident_id)
#             }, 404
