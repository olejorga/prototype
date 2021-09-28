from fastapi.testclient import TestClient
from fastapi.encoders import jsonable_encoder
from pysondb import db
from src.main import app
from src.models.item import Item

client = TestClient(app)

TEST_ITEM = Item(name="Sokk",
                 price=10,
                 description="Dette er en sokk",
                 pictures=["sokk.jpg"])

TEST_ITEM_JSON = jsonable_encoder(TEST_ITEM)


def test_read_items_view():
    response = client.get("/items/")
    assert response.status_code == 200


"""
def test_create_item():
    response = client.post("/api/items/", json=TEST_ITEM_JSON)
    id = response.json()
    items_db = db.getDb("data/items.json")
    test_item_in_db = items_db.find(id)

    del test_item_in_db[id]

    assert response.status_code == 200
    assert test_item_in_db == TEST_ITEM_JSON

    items_db.deleteById(id)
"""
