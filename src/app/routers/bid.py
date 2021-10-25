from typing import List
from fastapi import APIRouter, Request, Form, Cookie
from fastapi.responses import HTMLResponse, Response
from fastapi.templating import Jinja2Templates
from fastapi.exceptions import HTTPException
from ...core.entities.bid import Bid
from ..models.pickle_repository import PickleRepository


bids_repo = PickleRepository("data/bids.dat")
users_repo = PickleRepository("data/users.dat")

templates = Jinja2Templates(directory="src/app/templates")

router = APIRouter()


@router.get("/bids/my", tags=["bids", "view"], response_class=HTMLResponse)
async def read_sellers_listings_view(request: Request, user_token = Cookie(None)):
    user = users_repo.find(user_token)

    if user is None or user.get_class_name() != "Buyer":
        raise HTTPException(status_code = 403)
    
    return templates.TemplateResponse("bids.html", {
        "request": request,
        "title": "Mine bud",
        "bids": bids_repo.search("user_id", user.id)
    })


@router.post("/api/bids/{id}", tags=["bid", "api"])
async def create_bid(id: str, user_token = Cookie(None), amount: str = Form(...)):
    bid = Bid(id, user_token, amount)
    bids_repo.create(bid)
