from app.db.db_config import DbModel
from datetime import datetime, timedelta


class IncidentsModel(DbModel):
    """Incidents Model Class init"""

    def __init__(self, title=None, description=None,
                 incident_status=None, incident_type=None,
                 location=None, comment=None, createdBy=None):

        self.title = title
        self.title = description
        self.incident_type = incident_type
        self.location = location
        self.comment = comment
        self.incident_status = incident_status
        self.created_by = createdBy
        self.created_on = datetime.utcnow()

    def create_incident(self):
        query_string = "INSERT INTO incidents (title, description,  " +\
            "incident_type, location, comment, incident_status, created_by," +\
            " created_on) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"

        data = (self.title, self.description, self.incident_type,
                self.location, self.comment, self.incident_status,
                self.created_by, self.created_on,)

        # run query then commit record
        self.query(query_string, data)
        self.save()

        return {"message": "record saved successsfully"}
