import re


class ViewsValidation:

    # define check input fileds method
    def check_fields(self, resource_type="", field_data=None, field=None):
        # fields - list of fields to be checked
        # request.body recived at endpoint
        # extract fields into list

        # incidents fields validation
        if (resource_type == "red-flags" or "interventions"):
            fields = [
                'title',
                'description',
                'incident_status',
                'image',
                'video',
                'comment',
                'location'
            ]
        # patch fields validation
        if(field == "comment"):
            fields = ['comment']
        if(field == "location"):
            fields = ['location']
        if(field == "status"):
            fields = ['incident_status']

        # auth fields validation
        if(resource_type == "signup"):
            fields = ['username', 'email',
                      'password', 'phone_number', 'is_admin']
        if(resource_type == "login"):
            fields = ['email', 'password']
        if (resource_type == ""):
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

    def validate_id(self, id):
        try:
            int(id)
        except:
            return self.views_error(
                405,
                "ID must be an Integer"
            )

    def check_email(self, user_email):
        """
        method to validate email, via reg expressions
        """
        if not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", user_email):
            return "Invalid Email Format"
        if user_email == "":
            return "email cannot be blank"
        return False

    def check_phone_number(self, phone_number):
        """
        method to validate phone_number, via reg expressions
        """
        if not re.match(r"^([\s\d]+)$", phone_number):
            return "Invalid PhoneNumber Format, numbers only"
        if phone_number == "":
            return "phone_number cannot be blank."
        return False

    def check_username(self, username):
        """
        method to validate username, via reg expressions
        """
        if not re.match(r"[a-z A-Z0-9\_\"]+$", username):
            return "Invalid username Format, underscore, letters and numbers only"
        if username == "":
            return "username cannot be blank."
        return False

    def check_password(self, password):
        """
        method to validate password, via reg expressions
        """
        if not re.match(r"(((?=.*[a-z])(?=.*[A-Z]))|((?=.*[a-z])(?=.*[0-9]))|((?=.*[A-Z])(?=.*[0-9])))(?=.{8,})", password):
            return "Invalid Password Format, > 8 characters, letters, numbers and special character only "
        if password == "":
            return "password cannot be blank."
        return False

    def check_video_or_image_url(self, url):
        """
        method to validate video, password url, via reg expressions
        """
        if not re.match(r"([a-zA-Z0-9\s_\\.\-\(\):])+(.mp4|.mov|.mkv)$", url):
            return "Invalid Image Extension only [mp4,mkv,mov] allowed."
        if url == "":
            return "Invalid Video/Image url cannot be blank."
        return False

    def check_role(self, is_admin):
        """
        method to validate video, password url, via reg expressions
        """
        if is_admin not in ["True", "False"]:
            return "is_admin can only take in true of false"

    def check_fields_data(self, field_data):
        """
        validate all fields and return an errors object
        """
        # vaidator list to store all validation functions

        validator_fuctions = [
            self.check_email, self.check_phone_number,
            self.check_password, self.check_role, self.check_username
        ]

        # errors dict to store any errors if found
        errors = {}
        error = False

        print("Fields_Data::", field_data)

        for field, value in field_data.items():
            if field == "email":
                if validator_fuctions[0](value):
                    errors[field] = validator_fuctions[0](value)
                    print("Email::", value)
                    error = True
            if field == "phone_number":
                if validator_fuctions[1](value):
                    errors[field] = validator_fuctions[1](value)
                    print("Phonenumber::", value)
                    error = True
            if field == "password":
                if validator_fuctions[2](value):
                    errors[field] = validator_fuctions[2](value)
                    print("Password::", value)
                    error = True
            if field == "is_admin":
                if validator_fuctions[3](value):
                    errors[field] = validator_fuctions[3](value)
                    print("Admin::", value)
                    error = True
            if field == "username":
                if validator_fuctions[4](value):
                    errors[field] = validator_fuctions[4](value)
                    print("Username::", value)
                    error = True

        if error:
            return self.views_error(
                400,
                errors
            )
