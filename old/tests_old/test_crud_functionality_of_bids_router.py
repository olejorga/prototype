from fastapi.testclient import TestClient
from fastapi.encoders import jsonable_encoder
from pysondb import db
from src.main import app
from src.models.bid import Bid

bid_db = db.getDb("data/bids.json")

client = TestClient(app)


def test_read_bids_view():
    res = client.get("/bids/")
    assert res.status_code == 200


def test_read_bid_view():
    res = client.get("/bids/")
    assert res.status_code == 200


def test_create_new_bid_and_add_to_database():
    bid = Bid()
    res = client.post("/api/bids/", json=jsonable_encoder(bid))
    id = res.json()

    bid_from_db = bid_db.getBy({"id": id})[0]
    del bid_from_db["id"]

    assert res.status_code == 200
    assert bid_from_db == jsonable_encoder(bid)

    bid_db.deleteById(id)


def test_update_existing_bid_in_database():
    bid = Bid()
    id = bid_db.add(jsonable_encoder(bid))
    bid.bid_value = 1.0
    res = client.put("/api/bids/" + str(id), json=jsonable_encoder(bid))

    bid_from_db = bid_db.getBy({"id": id})[0]
    del bid_from_db["id"]

    assert res.status_code == 200
    assert bid_from_db == jsonable_encoder(bid)

    bid_db.deleteById(id)


def test_delete_existing_bid_from_database():
    bid = Bid()
    id = bid_db.add(jsonable_encoder(bid))
    res = client.delete("/api/bids/" + str(id))

    assert res.status_code == 200
    assert bid_db.getBy({"id": id}) == []
