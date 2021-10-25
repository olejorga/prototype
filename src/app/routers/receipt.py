from fastapi import APIRouter, Request
from fastapi.encoders import jsonable_encoder
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pysondb import db
from ..models.item import Item
from ..models.receipt import Receipt

receipt_db = db.getDb("data/receipt.json")

templates = Jinja2Templates(directory="src/templates")

router = APIRouter()


@router.get("/receipts/", tags=['receipts view'], response_class=HTMLResponse)
async def read_receipts_view(request: Request):
    return templates.TemplateResponse(
        "receipt.html", {
            "request": request,
            "title": "Receipts",
            "items": receipts_db.getAll()
        })


@router.get("/receipts/{id}", tags=['receipt view'], response_class=HTMLResponse)
async def read_receipt_view(id: int, request: Request):
    return templates.TemplateResponse(
        "receipt.html", {
            "request": request,
            "title": "Receipt",
            "receipt": receipt_db.getBy({"id": id})[0]
        })


@router.post("/api/receipts/", tags=['receipts api'])
async def create_receipt(receipt: Receipt):
    id = receipt_db.add(jsonable_encoder(receipt))
    return id

