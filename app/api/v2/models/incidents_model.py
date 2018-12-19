
from app.db.db_config import DbModel
from datetime import datetime, timedelta


class IncidentsModel(DbModel):
    """Incidents Model Class init"""

    def __init__(self, title=None, description=None,
                 incident_status=None, incident_type=None,
                 location=None, comment=None, image=None,
                 video=None, created_by=None):

        self.title = '' if title is None else title
        self.description = '' if description is None else description
        self.incident_type = incident_type
        self.location = '' if location is None else location
        self.comment = '' if comment is None else comment
        self.incident_status = (
            "Draft" if incident_status is None else incident_status
        )
        self.created_by = created_by
        self.image = [] if image is None else image
        self.video = [] if video is None else video
        self.created_on = datetime.utcnow()

        # instanciate the inherited DbModel class
        super().__init__()

    def create_incident(self):
        """method to insert new incident into database"""

        query_string = "INSERT INTO incidents (title, description,  " +\
            "incident_type, location, comment, incident_status, image" +\
            ", video ,created_by ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"

        data = (self.title, self.description, self.incident_type,
                self.location, self.comment, self.incident_status,
                self.image, self.video, self.created_by,)

        # run query then commit record
        self.query(query_string, data)
        self.save()

    def get_last_incident(self):
        query_string = "SELECT * from incidents " +\
            "ORDER BY created_on DESC LIMIT 1;"

        # query db
        self.query(query_string)

        # return queried records (single record)
        incident = self.find_one()

        if incident:
            return incident
        return None

    def get_all_incidents(self):
        query_string = "SELECT * from incidents;"

        # query db
        self.query(query_string)

        # return queried records (single record)
        incident = self.find_all()  # data
        fields = self.find_fields()  # fields

        incidents_list = []
        incident_data = {}

        for i in range(len(incident)):
            for index in range(len(fields)):
                if fields[index] == 'created_on':
                    incident_data.update(
                        {fields[index]: "{}".format(incident[i][index])})
                    continue
                incident_data.update({fields[index]: incident[i][index]})
            # append single incident dict into incidents list
            incidents_list.append(dict(incident_data))

        if incident:
            return incidents_list
        return None

    def get_incident_by(self, field, value, role=None):
        """method return incident based on field and data provided"""

        if role:  # admin user found: update any record
            query_string = "SELECT * from incidents WHERE {}=%s ".format(field)
            data = (value,)

        else:  # normal user found: update your records only
            query_string = "SELECT * from incidents WHERE {}".format(field) +\
                "=%s AND created_by=%s;"
            data = (value, self.created_by,)

        self.query(query_string, data)

        incident = self.find_all()

        fields = self.find_fields()

        incidents_list = []
        incident_data = {}

        for i in range(len(incident)):
            for index in range(len(fields)):
                if fields[index] == 'created_on':
                    incident_data.update(
                        {fields[index]: "{}".format(incident[i][index])})
                    continue
                incident_data.update({fields[index]: incident[i][index]})
            # append single incident dict into incidents list
            incidents_list.append(dict(incident_data))

        if incident:
            return incidents_list
        return None

    def delete_incident(self, field, value):
        """method to delete incident based on provided incident_field"""

        incident = self.get_incident_by(field, value)

        # delete user incidents only
        if incident:
            query_string = "DELETE from incidents WHERE {} ".format(field) +\
                "= %s AND created_by = %s;"

            data = (value, self.created_by,)

            self.query(query_string, data)
            self.save()

            return incident
        else:
            return None

    def update_incident(self, field, field_data, incident_id, role=None):
        """
        method to update incident based on provided
        incident_field, field_value and data
        """

        # does incident exist?
        incident = self.get_incident_by("incident_id", incident_id, role)

        if incident:
            if role:  # admin user found: update any record
                query_string = "UPDATE incidents SET " +\
                    "{}='{}' WHERE incident_id='{}';".format(
                        field, field_data, incident_id)
            else:  # normal user found: update your records only
                query_string = "UPDATE incidents SET " +\
                    "{}='{}' WHERE incident_id='{}' AND created_by={};".format(
                        field, field_data, incident_id, self.created_by)

            self.query(query_string)
            self.save()

            updated_incident = self.get_incident_by(
                "incident_id", incident_id, role)

            return updated_incident
        else:
            return None

    def can_update_or_delete(self, incident_id):
        """
        method to check incident status
        return true if incident_status == draft
        """
        incident = self.get_incident_by("incident_id", incident_id)

        if incident:
            if incident[0]["incident_status"] != "Draft":
                return False
            else:
                return True
        else:
            return True
