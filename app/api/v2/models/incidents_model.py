from app.db.db_config import DbModel
from datetime import datetime, timedelta


class IncidentsModel(DbModel):
    """Incidents Model Class init"""

    def __init__(self, title=None, description=None,
                 incident_status=None, incident_type=None,
                 location=None, comment=None, created_by=None):

        self.title = title
        self.title = description
        self.incident_type = incident_type
        self.location = location
        self.comment = comment
        self.incident_status = incident_status
        self.created_by = created_by
        self.created_on = datetime.utcnow()

    def create_incident(self):
        """method to insert new incident into database"""

        query_string = "INSERT INTO incidents (title, description,  " +\
            "incident_type, location, comment, incident_status, created_by," +\
            " created_on) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"

        data = (self.title, self.description, self.incident_type,
                self.location, self.comment, self.incident_status,
                self.created_by, self.created_on,)

        # run query then commit record
        self.query(query_string, data)
        self.save()

        return {"message": "record created successsfully"}

    def get_incident_by_id(self, incident_id):
        query_string = "SELECT * from incidents WHERE incident_id= %s"

        # query db
        self.query(query_string, (incident_id,))

        # return queried records (single record)
        incident = self.find_one()

        if incident:
            return incident
        return None

    def get_last_incident(self):
        query_string = "SELECT * from incidents ORDER BY TIMESTAMP DESC LIMIT 1"

        # query db
        self.query(query_string)

        # return queried records (single record)
        incident = self.find_one()

        if incident:
            return incident
        return None
