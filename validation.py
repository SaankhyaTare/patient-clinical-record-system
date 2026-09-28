from datetime import datetime


def valid_name(name):
    return name.strip() != ""


def valid_age(age):
    return age.isdigit() and 0 < int(age) <= 120


def valid_gender(gender):
    return gender.lower() in ["male", "female", "other"]


def valid_phone(phone):
    return phone.isdigit() and len(phone) == 10


def valid_date(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
        return True
    except ValueError:
        return False