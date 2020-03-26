import Utils.String as String


def validation(user):
    if user.email is not None and not String.check_email(user.email):
        raise Exception('Invalid Email Address')

    if user.mobile_number is not None and not String.check_mobile(user.mobile_number):
        raise Exception('Invalid Mobile Number')

