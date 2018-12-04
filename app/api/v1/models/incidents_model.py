
import datetime
from flask import json

incidents = []


class IncidentsModel():
    def __init__(self):
        self.dbase = incidents

    def save(self, incident_entry):
        """
        method to add new incident into incidents list
        """
        incident_data = {
            "id": len(self.dbase)+1,  # implements id auto increment feature
            "title": incident_entry["title"],
            "description": incident_entry["description"],
            "location": incident_entry["location"],
            "status": incident_entry["status"],
            "image": incident_entry["image"],
            "video": incident_entry["video"],
            "comment": incident_entry["comment"],
            "createdBy": incident_entry["createdBy"],
            "createdOn": str(datetime.datetime.now())
        }
        self.dbase.append(incident_data)
        return incident_data


# end of file past line 75 any methods will be ignored by ptyhon
# interpreter and the entire flask app :-(
