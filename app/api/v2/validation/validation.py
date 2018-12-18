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
        phone_number = phone_number.strip()
        if not re.match(r"^([\s\d]+)$", phone_number):
            return "Invalid PhoneNumber Format, numbers only"
        return False

    def check_username(self, username):
        """
        method to validate username, via reg expressions
        """
        username = username.strip()
        if not re.match(r"[a-z A-Z0-9\_\"]+$", username):
            return "Invalid username Format, underscore,"
            " letters and numbers only"
        return False

    def check_password(self, password):
        """
        method to validate password, via reg expressions
        """
        password = password.strip()
        if not re.match(r"(((?=.*[a-z])(?=.*[A-Z]))|((?=.*[a-z])(?=.*[0-9]))|((?=.*[A-Z])(?=.*[0-9])))(?=.{8,})", password):
            return "Invalid Password Format, > 8 characters, letters, " +\
                "numbers and special characters only "
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
        title = title.strip()
        if title == "":
            return "Title cannot be blank."
        else:
            return False

    # 2. description
    def check_description(self, description):
        description = description.strip()
        if description == "":
            return "Description cannot be blank"
        else:
            return False

    # 3. incident status
    def check_status(self, incident_status):
        incident_status = incident_status.strip()
        if incident_status not in [
            "Draft", "Under Investigation", "Resolved", "Rejected"
        ]:
            return "Invalid Status, [ Draft, Under Investigation," +\
                " Resolved, Rejected] only."
        else:
            return False

    # 4. location
    def check_location(self, location):
        """
        method to validate location, via reg expressions
        """
        location = location.strip()
        if not re.match(r"^[-+]?([1-8]?\d(\.\d+)?|90(\.0+)?),\s*[-+]?(180(\.0+)?|((1[0-7]\d)|([1-9]?\d))(\.\d+)?)$", location):
            return "Invalid location coordinates ."
        else:
            return False

    # 6. video
    def check_video_url(self, video_urls):
        """
        method to validate file path and image file extension, via reg expressions
        """
        video_urls = video_urls.strip()
        # loop through video path list
        for video_url in video_urls:
            # extract file name (abcde.mp4) from file path
            file_name = video_url.split("/")[-1]
            if not re.match(r"([a-zA-Z0-9\s_\\.\-\(\):])+(.mp4|.mov|.mkv|.3gp)$", file_name):
                return "Invalid Video Extension, " +\
                    "only [ .mp4, .mkv, .mov, .3gp ] allowed."
            else:
                return False

    # 5. image
    def check_image_url(self, image_urls):
        """
        method to validate file path and video file extension, via reg expressions
        """
        image_urls = image_urls.strip()
        # loop through video path list
        for image_url in image_urls:
            # extract file name (abcde.jpeg) from file path
            file_name = image_url.split("/")[-1]
            if not re.match(r"([a-zA-Z0-9\s_\\.\-\(\):])+(.jpg|.png|.jpeg|.gif)$", file_name):
                return "Invalid Image Extension, " +\
                    " only [.jpg, .png, .jpeg ] allowed."
            else:
                return False

    # 7. comment
    def check_comments(self, comment):
        """
        method to validate comments, via reg expressions
        """
        comment = comment.strip()
        if not re.match(r"^[a-zA-Z\d\-_\s,.;:\"']+$", comment):
            return "Invalid comments format."
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
            self.check_location, self.check_image_url, self.check_video_url,
            self.check_comments
        ]

        fields = [
            "email", "phone_number", "password",
            "is_admin", "username", "title", "description",
            "incident_status", "location", "image", "video", "comment"
        ]

        # errors dict to store any errors if found
        errors = {}
        error = False

        for field, value in field_data.items():
            for index in range(len(validator_fuctions)):
                if field == fields[index]:
                    if validator_fuctions[index](value):
                        errors[field] = validator_fuctions[index](value)
                        error = True

        if error:
            return self.views_error(
                400,
                errors
            )
