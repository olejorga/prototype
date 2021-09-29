from fastapi.testclient import TestClient
from fastapi.encoders import jsonable_encoder
from pysondb import db
from src.main import app
from src.models.item import Item

items_db = db.getDb("data/items.json")

client = TestClient(app)


def test_read_items_view():
    res = client.get("/items/")
    assert res.status_code == 200


def test_read_item_view():
    res = client.get("/items/")
    assert res.status_code == 200


def test_create_item():
    item = Item()
    res = client.post("/api/items/", json=jsonable_encoder(item))
    id = res.json()

    item_from_db = items_db.getBy({"id": id})[0]
    del item_from_db["id"]

    assert res.status_code == 200
    assert item_from_db == jsonable_encoder(item)

    items_db.deleteById(id)


def test_update_item():
    item = Item()
    id = items_db.add(jsonable_encoder(item))
    item.price = 1.0
    res = client.put("/api/items/" + str(id), json=jsonable_encoder(item))

    item_from_db = items_db.getBy({"id": id})[0]
    del item_from_db["id"]

    assert res.status_code == 200
    assert item_from_db == jsonable_encoder(item)

    items_db.deleteById(id)


def test_delete_item():
    item = Item()
    id = items_db.add(jsonable_encoder(item))
    res = client.delete("/api/items/" + str(id))

    assert res.status_code == 200
    assert items_db.getBy({"id": id}) == []
