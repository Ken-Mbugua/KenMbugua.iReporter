from flask import jsonify


class ViewsValidation:

    # define check input fileds method
    def missing_fields(self, fields, field_data):
        # fields - list of fields to be checked
        # request.body recived at enpoint
        # extract fields into list
        field_list = list(field_data.keys())
        missing_fields = [
            field for field in fields if field not in field_list]

        return missing_fields
