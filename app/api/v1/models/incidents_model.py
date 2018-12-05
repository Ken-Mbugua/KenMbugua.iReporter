
import datetime

incidents = []


class IncidentsModel():
    def __init__(self):
        self._dbase = incidents

    def save(self, incident_entry):
        """
        method to add new incident into incidents list
        """
        incident_data = {
            "id": len(self._dbase)+1,  # implements id auto increment feature
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

        incident = self.get_incident_by_id(incident_data["id"])

        if incident:
            return None  # incident already exists
        else:
            self._dbase.append(incident_data)
            return incident_data

    def get_incidents(self):
        """
        method to get all incidences
        """
        if not self._dbase:
            return None
        else:
            return self._dbase

    def get_incident_by_id(self, incident_id):
        """
        method to a single incident record
        """
        all_incidents = self._dbase         # get all incidents
        # loop through the incidents to find an id match
        for incident in all_incidents:
            # id found success return unique incident
            if (incident_id == incident["id"]):
                return incident

    def get_incident_by_name(self, incident_title):
        """
        method to a single incident record
        """
        all_incidents = self._dbase         # get all incidents
        # loop through the incidents to find an id match
        for incident in all_incidents:
            # id found success return unique incident
            if (incident_title == incident["title"]):
                return incident

    def delete_incident(self, incident_id):
        """
        method to delete single incident
        """
        new_incidents = self._dbase     # copy incidents dictonary
        for incident in new_incidents:  # look for incident by id
            if(incident_id == incident["id"]):  # incident found now remove it
                new_incidents.pop(incident_id-1)  # remove item at pop(1d-1)
                return incident

    def edit_incident(self, incident_id, data):
        # filter incidents by id
        incident = self.get_incident_by_id(incident_id)
        if incident:
            # if found update list
            incident.update(data)
            return incident

    @staticmethod
    def update_incident(incident_id, data):
        new_incident_instance = IncidentsModel()
        incident = new_incident_instance.get_incident_by_id(incident_id)
        if incident:
            incident.update(data)
            return incident

# end of file past line 75 any methods will be ignored by ptyhon
# interpreter and the entire flask app :-(
