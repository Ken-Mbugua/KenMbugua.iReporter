

class ModelValidation:
    def __init__(self):
        self.valid = True

    # def user_details_validate(self, user_data):
    #     """
    #     validate all user fields for correct types
    #     """
    #     # check for only these fields only allow these fields through
    #     # -- [ firstname, lastname, othername,email,
    #           password, phonenumber ] --
    #     # auto generated fileds [registered = Date ]
    #     # [isAdmin default False] updated via protected route
    #     # firstname, username, lastname = String
    #     # step - 1 check for fields threshold
    #     # step - 2 check for fields valid data

    #     for user_field in user_data:
    #         if user_field

    def check_duplicate_record(self, record_id, db_list):
        """
        validate if there is a duplicate record
        """
        for record in db_list:
            if record_id == db_list["id"]:
                return record  # return same record if theres a duplicate
        return None
