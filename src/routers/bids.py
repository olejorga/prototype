from fastapi import APIRouter, Request
from fastapi.encoders import jsonable_encoder
from pysondb import db
from starlette.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from ..models.bid import Bid

bid_db = db.getDb("data/bids.json")

templates = Jinja2Templates(directory="src/templates")

router = APIRouter()


# TODO get item id as a variable on each bid.
@router.get("/bids/", tags=['bids view'], response_class=HTMLResponse)
async def read_bids_view(request: Request):
    return templates.TemplateResponse(
        "bids.html", {
            "request": request,
            "title": "bids",
            "bids": bid_db.getAll()
        })


@router.get("/bids/{id}", tags=['bids view'], response_class=HTMLResponse)
async def read_bid_view(bid_id: int, request: Request):
    return templates.TemplateResponse(
        "bids.html", {
            "request": request,
            "title": "Bids",
            "item": bid_db.getBy({"id": bid_id})
        })


@router.post("/api/bids/", tags=['bids api'])
async def create_bid(bid: Bid):
    id = bid_db.add(jsonable_encoder(bid))
    return id


@router.put("/api/bids/{id}", tags=['bids api'])
async def update_bid(id: int, bid: Bid):
    bid_db.updateById(id, jsonable_encoder(bid))
    return id


@router.delete("/api/bids/{id}", tags=['bids api'])
async def delete_bid(id: int):
    id = bid_db.deleteById(id)
    return id
