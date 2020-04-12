class GetAllUserByPaginationResponse:
    def __init__(self, user, addresses):
        self.id = user.id
        self.code = user.code
        self.fullname = user.fullname
        self.mobile_number = user.mobile_number
        self.birth_date = user.birth_date
        self.email = user.email
        self.status = user.status
        self.creation_date = user.creation_date
        self.modified_date = user.modified_date
        self.addresses = addresses


class AddressDto:
    def __init__(self, address):
        self.id = address.id
        self.country_name = address.country_name
        self.city_name = address.city_name
        self.postal_code = address.postal_code
        self.more_address = address.more_address
        self.creation_date = address.creation_date
        self.modified_date = address.modified_date
