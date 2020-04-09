import re


def check_email(email):
    pattern = r"([^@|\s]+@[^@]+\.[^@|\s]+)"

    return bool(re.match(f"{pattern}", email))


def check_mobile(mobile):
    pattern = r"(^09\d{9}$)"

    return bool(re.match(f"{pattern}", mobile))
