import Utils.String as String


def validation(request):
    if request.email is not None and not String.check_email(request.email):
        raise Exception('Invalid Email Address')

    if request.mobile_number is not None and not String.check_mobile(request.mobile_number):
        raise Exception('Invalid Mobile Number')
