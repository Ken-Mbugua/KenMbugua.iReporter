from flask import jsonify


class ViewsValidation:

    # define check input fileds method
    def check_fields(self, resource_type=None, field_data=None):
        # fields - list of fields to be checked
        # request.body recived at endpoint
        # extract fields into list
        if (resource_type == "red-flags" or "interventions"):
            fields = [
                'title',
                'description',
                'incident_status',
                'incident_type',
                'comment',
                'location'
            ]
        elif(resource_type == "signup"):
            fields = ['username', 'email', 'password', 'phone_number']
        elif(resource_type == "login"):
            fields = ['email', 'password']
        else:
            return self.views_error(
                400,
                "Invalid fields !"
            )

        field_list = list(field_data.keys())
        missing_fields = [
            field for field in fields if field not in field_list
        ]

        extra_fields = [
            field for field in field_list if field not in fields
        ]

        if missing_fields:
            return self.views_error(
                400,
                "Missing fields {}".format(missing_fields)
            )
        if extra_fields:
            return self.views_error(
                400,
                "Invalid fields {}".format(extra_fields)
            )
        else:
            return None

    def views_error(self, status, error_message="error", field="error"):
        return {
            "status": status,
            field: error_message
        }, status
