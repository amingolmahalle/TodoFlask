class EditUserRequest:

    def __init__(self,
                 id,
                 fullname,
                 mobile_number,
                 birth_date,
                 email,
                 status,
                 addresses):
        self.id = id
        self.fullname = fullname
        self.mobile_number = mobile_number
        self.birth_date = birth_date
        self.email = email
        self.status = status
        self.addresses = addresses
