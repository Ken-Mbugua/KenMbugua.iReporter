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
        """
        method to validate endpoint id
        """
        try:
            int(id)
        except:
            return self.views_error(
                405,
                "ID must be an Integer"
            )

    # incident_fields data validation

    def check_email(self, user_email):
        """
        method to validate email, via reg expressions
        """
        if not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", user_email):
            return "Invalid Email Format"

    def check_phone_number(self, phone_number):
        """
        method to validate phone_number, via reg expressions
        """
        if not re.match(r"^([\s\d]+)$", phone_number):
            return "Invalid PhoneNumber Format, numbers only"
        return False

    def check_username(self, username):
        """
        method to validate username, via reg expressions
        """
        if not re.match(r"[a-z A-Z0-9\_\"]+$", username):
            return "Invalid username Format, underscore,"
            " letters and numbers only"
        return False

    def check_password(self, password):
        """
        method to validate password, via reg expressions
        """
        if not re.match(r"(((?=.*[a-z])(?=.*[A-Z]))|((?=.*[a-z])(?=.*[0-9]))|((?=.*[A-Z])(?=.*[0-9])))(?=.{8,})", password):
            return "Invalid Password Format, > 8 characters, letters, "
            "numbers and special character only "
        return False

    def check_role(self, is_admin):
        """
        method to validate video, password url, via reg expressions
        """
        if is_admin not in ["True", "False"]:
            return "is_admin can only take in 'True' of 'False'"

    # incident_fields data validation

    # 1. title
    def check_title(self, title):
        if title == "":
            return "Title cannot be blank."
        else:
            return False

    # 2. description
    def check_description(self, description):
        if description == "":
            return "Description cannot be blank"
        else:
            return False

    # 3. incident status
    def check_status(self, incident_status):
        if incident_status not in [
            "Draft", "Under Investigation", "Resolved", "Rejected"
        ]:
            return "Invalid Status, Draft, Under Investigation,"
            " Resolved, Rejected only."
        else:
            return False

    # 4. location
    def check_location(self, location):
        """
        method to validate location, via reg expressions
        """

        if not re.match(r"^[-+]?([1-8]?\d(\.\d+)?|90(\.0+)?),\s*[-+]?(180(\.0+)?|((1[0-7]\d)|([1-9]?\d))(\.\d+)?)$", location):
            return "Invalid location coordinates ."
        else:
            return False

    # 5. image # 6. video
    def check_video_or_image_url(self, url):
        """
        method to validate video and image extension, via reg expressions
        """
        if not re.match(r"([a-zA-Z0-9\s_\\.\-\(\):])+(.mp4|.mov|.mkv|.3gp)$", url):
            return "Invalid Image Extension only [ mp4,mkv,mov,3gp ] allowed."
        return False

    # 7. comment
    def check_comments(self, comment):
        """
        method to validate comments, via reg expressions
        """
        if not re.match(r"^[a-zA-Z\d\-_\s,.;:\"']+$", comment):
            return True
        return False

    def check_fields_data(self, field_data):
        """
        validate all fields and return an errors object
        """
        # vaidator list to store all validation functions

        validator_fuctions = [
            self.check_email, self.check_phone_number,
            self.check_password, self.check_role, self.check_username,
            self.check_title, self.check_description, self.check_status,
            self.check_location, self.check_video_or_image_url,
            self.check_comments
        ]

        # errors dict to store any errors if found
        errors = {}
        error = False

        print("Fields_Data::", field_data)

        for field, value in field_data.items():
            if field == "email":
                if validator_fuctions[0](value):
                    errors[field] = validator_fuctions[0](value)

                    error = True
            if field == "phone_number":
                if validator_fuctions[1](value):
                    errors[field] = validator_fuctions[1](value)

                    error = True
            if field == "password":
                if validator_fuctions[2](value):
                    errors[field] = validator_fuctions[2](value)

                    error = True
            if field == "is_admin":
                if validator_fuctions[3](value):
                    errors[field] = validator_fuctions[3](value)

                    error = True
            if field == "username":
                if validator_fuctions[4](value):
                    errors[field] = validator_fuctions[4](value)

                    error = True
            if field == "title":
                if validator_fuctions[5](value):
                    errors[field] = validator_fuctions[5](value)
                    print("title::", value)
                    error = True
            if field == "description":
                if validator_fuctions[6](value):
                    errors[field] = validator_fuctions[6](value)
                    print("description::", value)
                    error = True
            if field == "incident_status":
                if validator_fuctions[7](value):
                    errors[field] = validator_fuctions[7](value)
                    print("status::", value)
                    error = True
            if field == "location":
                if validator_fuctions[8](value):
                    errors[field] = validator_fuctions[8](value)
                    print("location::", value)
                    error = True
            if field == "image":
                if validator_fuctions[9](value):
                    errors[field] = validator_fuctions[9](value)
                    print("image::", value)
                    error = True
            if field == "video":
                if validator_fuctions[9](value):
                    errors[field] = validator_fuctions[9](value)
                    print("video::", value)
                    error = True
            if field == "comments":
                if validator_fuctions[10](value):
                    errors[field] = validator_fuctions[10](value)
                    print("comments::", value)
                    error = True

        if error:
            return self.views_error(
                400,
                errors
            )
