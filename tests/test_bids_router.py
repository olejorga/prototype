from fastapi.testclient import TestClient
from fastapi.encoders import jsonable_encoder
from pysondb import db
from src.main import app
from src.models.bid import Bid

bid_db = db.getDb("data/bids.json")

client = TestClient(app)

def test_read_bid_view():
    res = client.get("/bids/")
    assert res.status_code == 200