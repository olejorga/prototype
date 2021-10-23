from fastapi import APIRouter, Request
from fastapi.encoders import jsonable_encoder
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from pysondb import db

from ..models.item import Item

items_db = db.getDb("data/items.json")

templates = Jinja2Templates(directory="src/templates")

router = APIRouter()


@router.get("/ny annonse/", tags=['items view'], response_class=HTMLResponse)
async def read_items_view(request: Request):
    return templates.TemplateResponse("items.html", {
        "request": request,
        "title": "Ny annonse"
    })
