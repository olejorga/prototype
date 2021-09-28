from fastapi.testclient import TestClient
from fastapi.encoders import jsonable_encoder
from pysondb import db
from src.main import app
from src.models.item import Item

TEST_ITEM = Item(name="Sokk",
                 price=10,
                 description="Dette er en sokk",
                 pictures=["sokk.jpg"])

TEST_ITEM_JSON = jsonable_encoder(TEST_ITEM)

items_db = db.getDb("data/items.json")

client = TestClient(app)


def test_read_items_view():
    response = client.get("/items/")
    assert response.status_code == 200
