from fastapi import APIRouter, Request
from fastapi.encoders import jsonable_encoder
from pysondb import db
from starlette.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from .items import items_db
from ..models.bid import Bid
from ..models.item import Item

bids_db = db.getDb("data/bids.json")

templates = Jinja2Templates(directory="src/templates")

router = APIRouter()


@router.get("/bids/", tags=['bids view'], response_class=HTMLResponse)
async def read_bids_view(request: Request):
    return templates.TemplateResponse(
        "bids.html", {
            "request": request,
            "title": "bids",
            "bids": bids_db.getAll()
        })


@router.post("/api/bids/", tags=['bids api'])
async def create_bid(bid: Bid):
    bid_id = bids_db.add(jsonable_encoder(bid))
    return bid_id


@router.put("/api/bids/{id}", tags=['bids api'])
async def update_bid(bid_id: int, bid: Bid):
    bids_db.updateById(bid_id, jsonable_encoder(bid))
    return bid_id


@router.delete("/api/bids/{id}", tags=['bids api'])
async def delete_bid(bid_id: int):
    bid_id = bids_db.deleteById(bid_id)
    return bid_id
