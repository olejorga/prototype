from fastapi.testclient import TestClient
from src.components.item_func import *
import datetime


def test_countdown_for_ongoing_auctions():
    assert countdown(datetime.datetime.now()) == datetime.timedelta(0)
    assert countdown(datetime.datetime.now() + datetime.timedelta(days=1, hours=3)) == datetime.timedelta(days=1,
                                                                                                          hours=3)
