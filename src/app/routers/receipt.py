from typing import List
from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, Response, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.exceptions import HTTPException

from ...core.entities.receipt import Receipt
from ...core.entities.listing import Listing
from ..models.pickle_repository import PickleRepository

listings_repo = PickleRepository("data/listings.dat")
users_repo = PickleRepository("data/users.dat")
receipt_repo = PickleRepository("data/receipts.dat")

templates = Jinja2Templates(directory="src/app/templates")

router = APIRouter()

@router.get("/receipts/", tags=["receipts", "view"], response_class=HTMLResponse)
async def read_receipt_view(request: Request):
    user = request.state.current_user
    
    if user is None or user.get_class_name() == "Admin":
        raise HTTPException(status_code=403)

    return templates.TemplateResponse("receipts.html", {
        "request": request,
        "title": "Kvittering",
        "receipts": receipt_repo.read()
    })


@router.get("/receipts/{id}", tags=["receipt", "view"], response_class=HTMLResponse)
async def read_receipt(request: Request, id: str):
    receipt = receipt_repo.find(id)

    return templates.TemplateResponse("receipt.html",{
        "request": request,
        "title": "Kvittering",
        "receipt": receipt
    })


@router.post("/api/receipt/{id}", tags=["receipts", "api"])
async def create_receipt(response: Response, request: Request, id: str):
    user = request.state.current_user

    if user is None or user.get_class_name() != "Buyer":
        raise HTTPException(status_code = 403)
    
    listing = listings_repo.find(id)
    receipt = Receipt(listing)
    receipt_repo.create(receipt)

    response = RedirectResponse(url="/receipts/")
    response.status_code = 302
    
    return response