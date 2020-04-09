from datetime import datetime


def utc_now(format_date=None):
    return datetime.utcnow().isoformat() if format_date is None else datetime.utcnow().strftime(f"{format_date}")


def now(format_date=None):
    return datetime.now().isoformat() if format_date is None else datetime.now().strftime(f"{format_date}")


def convert_string_to_datetime(date_string, format_date='%Y-%m-%dT%H:%M:%SZ'):
    return datetime.strptime(date_string, format_date)
