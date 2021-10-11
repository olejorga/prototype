import datetime


def countdown(auction_date: datetime):
    """
    Return-type timedelta
    https://docs.python.org/3/library/datetime.html
    """

    current_date = datetime.datetime.now()

    return auction_date - current_date

