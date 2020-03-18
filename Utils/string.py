import re


def check_email(email):
    pattern = r"([^@|\s]+@[^@]+\.[^@|\s]+)"

    return re.match(f"{pattern}", email)


def check_mobile(mobile):
    pattern = r"^((\+|00)?98|0)?(?<number>9\d{9})$"

    return re.match(f"{pattern}", mobile)
