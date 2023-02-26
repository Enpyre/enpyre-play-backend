import datetime


def get_current_week():
    today = datetime.date.today()
    return today.isocalendar()[1]


def get_current_month():
    today = datetime.date.today()
    return today.month


def get_current_year():
    today = datetime.date.today()
    return today.year
