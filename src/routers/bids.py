from fastapi import APIRouter, Request
from fastapi.encoders import jsonable_encoder
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from pysondb import db
from pysondb.db import DataNotFoundError

from ..models.bid import Bid, UpdateBid

bid_db = db.getDb("data/bids.json")

templates = Jinja2Templates(directory="src/templates")

router = APIRouter()


@router.get("/bids/", tags=['bids view'], response_class=HTMLResponse)
async def read_bids_view(request: Request):
    return templates.TemplateResponse("bids.html", {
        "request": request,
        "title": "bids",
        "bids": bid_db.getAll()
    })


# item_id gets parsed into this after pressing "Kjøp"
@router.get("/bids/{id}", tags=['bids view'], response_class=HTMLResponse)
async def read_bid_view(bid_id: int, request: Request):
    return templates.TemplateResponse("bids.html", {
        "request": request,
        "title": "Bids",
        "item": bid_db.getBy({"id": bid_id})
    })


# include user_id from form in item.html in someway, then a bid_to_update can be set to both the item_id and user_id
@router.post("/api/bids/{item_id}", tags=['bids api'])
async def create_bid(bids_item_id: int, bid: Bid):
    bid.set_item_id(bids_item_id)
#    bid.set_user_id(parameter)
#    bid.set_bid_value(parameter)
    return str(bid_db.add(jsonable_encoder(bid)))


@router.put("/api/bids/{bid_id}", tags=['bids api'])
async def update_bid(bid_id, bid_to_update: UpdateBid):
    if bid_to_update.get_bid_value() is not None:
        bid_db.updateById(bid_id, {"bid_value": bid_to_update.get_bid_value()})

    if bid_to_update.get_user_id is not None:
        bid_db.updateById(bid_id, {"user_id": bid_to_update.get_user_id()})

    return bid_id


@router.delete("/api/bids/{id}", tags=['bids api'])
async def delete_bid(id):
    id = bid_db.deleteById(id)
    return id
