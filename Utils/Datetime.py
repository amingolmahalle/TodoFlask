from datetime import datetime


def utc_now(format_date=None):
    return datetime.utcnow() if format_date is None else datetime.utcnow().strftime(f"{format_date}")


def now(format_date=None):
    return datetime.now() if format_date is None else datetime.now().strftime(f"{format_date}")
