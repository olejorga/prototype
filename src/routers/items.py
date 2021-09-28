# Importing FastAPI modules
from fastapi import APIRouter, Request
from fastapi.encoders import jsonable_encoder
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

# Importing pysondb
from pysondb import db

# Importing models
from ..models.item import Item

# Loading stored databases
items_db = db.getDb("data/items.json")

# Loading template-html-files
templates = Jinja2Templates(directory="src/templates")

##########
# ROUTES #
##########

router = APIRouter()


@router.get("/items/", tags=["items"], response_class=HTMLResponse)
async def read_items_view(request: Request):
    return templates.TemplateResponse(
        "items.html", {
            "request": request,
            "title": "Items",
            "items": items_db.getAll()
        })


@router.post("/api/items/", tags=["items"], )
async def create_item(item: Item):
    id = items_db.add(jsonable_encoder(item))
    return id


@router.put("/api/items/{id}", tags=["items"])
async def update_item_by_id(id: int, item: Item):
    items_db.updateById(id, jsonable_encoder(item))
    return id
