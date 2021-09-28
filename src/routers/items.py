from fastapi import APIRouter, Request
from fastapi.encoders import jsonable_encoder
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pysondb import db
from ..models.item import Item

items_db = db.getDb("data/items.json")

templates = Jinja2Templates(directory="src/templates")

router = APIRouter()


@router.get("/items/", tags=["items"], response_class=HTMLResponse)
async def read_items_view(request: Request):
    return templates.TemplateResponse(
        "items.html", {
            "request": request,
            "title": "Items",
            "items": items_db.getAll()
        })


@router.get("/api/items/", tags=["items"], response_model=list[Item])
async def read_items():
    return items_db.getAll()


@router.get("/api/items/{id}", tags=["items"], response_model=Item)
async def read_item(id: int):
    return items_db.getBy({"id"})


@router.post("/api/items/", tags=["items"])
async def create_item(item: Item):
    id = items_db.add(jsonable_encoder(item))
    return id


@router.put("/api/items/{id}", tags=["items"])
async def replace_item(id: int, item: Item):
    items_db.updateById(id, jsonable_encoder(item))
    return id


@router.patch("/api/items/{id}", tags=["items"])
async def modify_item(id: int, item: dict):
    items_db.updateById(id, jsonable_encoder(item))
    return id


@router.delete("/api/items/{id}", tags=["items"], )
async def delete_item(id: int):
    id = items_db.deleteById(id)
    return id
