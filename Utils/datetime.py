from datetime import datetime


def datetime_now_utc(format_date=None):
    return datetime.utcnow() if format_date is None else datetime.utcnow().strftime(f"{format_date}")


def datetime_now(format_date=None):
    return datetime.now() if format_date is None else datetime.now().strftime(f"{format_date}")
