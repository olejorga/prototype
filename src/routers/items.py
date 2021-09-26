from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from pysondb import db
from ..models.item import Item

items_db = db.getDb("data/items.json")

router = APIRouter()


@router.get("/api/items/", tags=["items"], response_model=list[Item])
async def read_all_items():
    return items_db.getAll()


@router.get("/api/items/{id}", tags=["items"], response_model=Item)
async def read_item_by_id(id: int):
    return items_db.find(id)


@router.post("/api/items/", tags=["items"])
async def create_item(item: Item):
    items_db.add(jsonable_encoder(item))


@router.put("/api/items/{id}", tags=["items"])
async def update_item_by_id(id: int, item: Item):
    items_db.updateById(id, jsonable_encoder(item))
