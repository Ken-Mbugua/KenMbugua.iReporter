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
        if re.match(r"(((?=.*[a-z])(?=.*[A-Z]))|((?=.*[a-z])(?=.*[0-9]))|((?=.*[A-Z])(?=.*[0-9])))(?=.{8,})", user_email):
            return "Invalid Email Format"
        if user_email == "":
            return "email cannot be blank"
        return False

    def check_phone_number(self, phone_number):
        """
        method to validate phone_number, via reg expressions
        """
        if re.match(r"(((?=.*[a-z])(?=.*[A-Z]))|((?=.*[a-z])(?=.*[0-9]))|((?=.*[A-Z])(?=.*[0-9])))(?=.{8,})", phone_number):
            return "Invalid PhoneNumber Format"
        if phone_number == "":
            return "phone_number cannot be blank."
        return False

    def check_password(self, password):
        """
        method to validate password, via reg expressions
        """
        if re.match(r"(((?=.*[a-z])(?=.*[A-Z]))|((?=.*[a-z])(?=.*[0-9]))|((?=.*[A-Z])(?=.*[0-9])))(?=.{8,})", password):
            return "Invalid Password Format."
        if password == "":
            return "password cannot be blank."
        return False

    def check_video_or_image_url(self, url):
        """
        method to validate video, password url, via reg expressions
        """
        if re.match(r"([a-zA-Z0-9\s_\\.\-\(\):])+(.mp4|.mov|.mkv)$", url):
            return "Invalid Image Extension only [mp4,mkv,mov] allowed."
        if url == "":
            return "Invalid Video/Image url cannot be blank."
        return False

    def check_role(self, is_admin):
        """
        method to validate video, password url, via reg expressions
        """
        if is_admin not in [True, False]:
            return False
        if is_admin == "":
            return "is_admin can only take in true of false"

    def check_fields_data(self, field_data):
        """
        validate all fields and return an errors object
        """
        # errors dict to store any errors if found
        errors = {}
        error = False

        for field in field_data:

            error = True

        if error:
            return errors
