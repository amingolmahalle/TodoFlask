from Domain.Entity.UserAggregate.User import User
from Domain.Entity.UserAggregate.Address import Address
from munch import munchify
import uuid


class AddUserFactory:

    @staticmethod
    def Map_to_Entity(request):
        code = str(uuid.uuid4()),
        fullname = request.fullname,
        mobile_number = request.mobile_number,
        birth_date = request.birth_date,
        email = request.email,
        status = True

        user = User(
            code=code,
            fullname=fullname,
            mobile_number=mobile_number,
            birth_date=birth_date,
            email=email,
            status=status)

        for address in munchify(request.addresses):
            country_name = address.country_name
            city_name = address.city_name
            postal_code = address.postal_code
            more_address = address.more_address

            address = Address(
                country_name,
                city_name,
                postal_code,
                more_address)

            user.addresses.append(address)

        return user
