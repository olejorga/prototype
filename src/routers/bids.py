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


# include user_id from form in item.html in someway, then a bid can be set to both the item_id and user_id
@router.post("/api/bids/{item_id}", tags=['bids api'])
async def create_bid(bids_item_id: int, bid: Bid):
    bid.item_id = bids_item_id
#    bid.user_id = parameter
    bid_id = bid_db.add(jsonable_encoder(bid))
    return bid_id


@router.put("/api/bids/{bid_id}", tags=['bids api'])
async def update_bid(bid_id: int, bid: UpdateBid):
    if bid.bid_value is not None:
        bid_db.updateById(bid_id, {"bid_value": bid.bid_value})

    if bid.user_id is not None:
        bid_db.updateById(bid_id, {"user_id": bid.user_id})

    return bid_id


@router.delete("/api/bids/{id}", tags=['bids api'])
async def delete_bid(id: int):
    id = bid_db.deleteById(id)
    return id
