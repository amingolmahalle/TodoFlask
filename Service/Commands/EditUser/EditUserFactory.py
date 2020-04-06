from Domain.Entity.UserAggregate.Address import Address
import Utils.Datetime as Datetime
from munch import munchify


class EditUserFactory:

    @staticmethod
    def Map_to_Entity(request, current_user):
        if current_user is not None:
            current_user.fullname = request.fullname if request.fullname is not None else current_user.fullname
            current_user.mobile_number = request.mobile_number if request.mobile_number is not None else current_user.mobile_number
            current_user.birth_date = request.birth_date
            current_user.email = request.email if request.email is not None else current_user.email
            current_user.status = request.status if request.status is not None else current_user.status
            current_user.modified_date = Datetime.utc_now()

        user = current_user

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
