from Models.Domain.User import User
from Models.Domain.Address import Address


def create(response):
    map_user = User(response[0]['code'], response[0]['fullname'], response[0]['mobile_number'],
                    response[0]['birth_date'], response[0]['email'], response[0]['status'],
                    response[0]['user_id'], response[0]['creation_date'], response[0]['modified_date'])

    for item in response:
        map_address = Address(item['country_name'], item['city_name'], item['postal_code'], item['more_address'],
                              item['address_id'], item['user_id'], item['creation_date'], item['modified_date'])

        map_user.addresses.append(map_address)

    return map_user
