import re


def check_email(email):
    pattern = r"([^@|\s]+@[^@]+\.[^@|\s]+)"

    return re.compile(pattern).match(email)


def check_mobile(mobile):
    pattern = r"(^(09)[0-9]{9}$)"

    return re.compile(pattern).match(mobile)
