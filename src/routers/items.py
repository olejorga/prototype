from fastapi import APIRouter, Request
from fastapi.encoders import jsonable_encoder
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pysondb import db
from ..models.item import Item

items_db = db.getDb("data/items.json")

templates = Jinja2Templates(directory="src/templates")

router = APIRouter()


@router.get("/items/", response_class=HTMLResponse)
async def read_items_view(request: Request):
    return templates.TemplateResponse(
        "items.html", {
            "request": request,
            "title": "Items",
            "items": items_db.getAll()
        })


@router.get("/items/{id}", response_class=HTMLResponse)
async def read_item_view(id: int, request: Request):
    return templates.TemplateResponse(
        "item.html", {
            "request": request,
            "title": "Item",
            "item": items_db.getBy({"id": id})
        })


@router.post("/api/items/")
async def create_item(item: Item):
    id = items_db.add(jsonable_encoder(item))
    return id


@router.put("/api/items/{id}")
async def replace_item(id: int, item: Item):
    items_db.updateById(id, jsonable_encoder(item))
    return id


@router.delete("/api/items/{id}")
async def delete_item(id: int):
    id = items_db.deleteById(id)
    return id
