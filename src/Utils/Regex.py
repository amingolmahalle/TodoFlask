import re


def check_email(value):
    pattern = r"([^@|\s]+@[^@]+\.[^@|\s]+)"

    return re.compile(pattern).match(value)


def check_mobile_format(value):
    pattern = r"^(09)[0-9]{9}$"

    return re.compile(pattern).match(value)


def check_phone_format(value):
    pattern = r"^(0)[1-8][0-9]{9}$"

    return re.compile(pattern).match(value)


def check_date_time_format(value):
    pattern = r"\d{4}-\d?\d-\d?\d (?:2[0-3]|[01]?[0-9]):[0-5]?[0-9]:[0-5]?[0-9]"

    return re.compile(pattern).match(value)


def check_alpha_format(value):
    pattern = r"^[a-zA-Z\\s]+$"

    return re.compile(pattern).match(value)


def check_numeric_format(value):
    pattern = r"^[0-9]+$"

    return re.compile(pattern).match(value)


def check_alpha_numeric_format(value):
    pattern = r"^[a-zA-Z0-9\\s]+$"

    return re.compile(pattern).match(value)


def check_alpha_dash_format(value):
    pattern = r"^[a-zA-Z]+[\\-_a-zA-Z0-9]+$"

    return re.compile(pattern).match(value)


def check_username_format(value):
    pattern = r"^[a-zA-Z]+[_a-zA-Z0-9.]+$"

    return re.compile(pattern).match(value)
