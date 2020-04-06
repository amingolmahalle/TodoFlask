class AddUserRequest:

    def __init__(self,
                 fullname,
                 mobile_number,
                 birth_date,
                 email,
                 addresses):
        self.fullname = fullname
        self.mobile_number = mobile_number
        self.birth_date = birth_date
        self.email = email
        self.addresses = addresses
