from Services.Validations.UserValidation import validation
import Repositories.UserRepository as userRepository
import Repositories.AddressRepository as addressRepository
import Services.Mapping.UserMapper as UserMapper
import Utils.Datetime as Datetime


def get_all_by_pagination(page, per_page):
    return userRepository.get_all_by_pagination(page, per_page)


def get_by_id_with_query(userId):
    result = None
    response = userRepository.get_by_id_with_query(userId)

    if len(response) > 0:
        result = UserMapper.create(response)

    return result


def get_all():
    response = userRepository.get_all()

    return response


def get_by_id(id):
    response = userRepository.get_by_id(id)

    return response


def get_by_mobile(mobile):
    response = userRepository.get_by_mobile(mobile)

    return response


def add(user):
    validation(user)
    # validation address

    userRepository.add(user)
    addressRepository.add_range(user.addresses)

    userRepository.commit()

    return user


def edit(id, user):
    validation(user)

    current_user = userRepository.get_by_id(id)

    if current_user is not None:
        current_user.fullname = user.fullname if user.fullname is not None else current_user.fullname
        current_user.mobile_number = user.mobile_number if user.mobile_number is not None else current_user.mobile_number
        current_user.birth_date = user.birth_date
        current_user.email = user.email if user.email is not None else current_user.email
        current_user.status = user.status if user.status is not None else current_user.status
        current_user.modified_date = Datetime.utc_now()
        # current_user.addresses.extend(user.addresses)

        # addressRepository.add_range(user.addresses)

        userRepository.commit()

    return current_user


def delete_by_id(id):
    user = userRepository.get_by_id(id)

    userRepository.delete(user)

    userRepository.commit()

    return 'OK!'
