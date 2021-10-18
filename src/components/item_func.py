from models import item, receipt
import datetime


def countdown(auction_date: datetime):
    """
    Return-type timedelta
    https://docs.python.org/3/library/datetime.html
    """

    current_date = datetime.datetime.now()

    return auction_date - current_date


def create_receipt(name: str, price: int):
    """
    Get price of item and date of sale and make a new receipt
    """
    return {
        id: 0,
        date: datetime.datetime.now(),
        procut_name: item.getName(),
        price: item.getPrice()
    }

