from typing import List
from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from ...core.entities.listing import Listing
from ..models.pickle_repository import PickleRepository


listings_repo = PickleRepository("data/listings.dat")

templates = Jinja2Templates(directory="src/app/templates")

router = APIRouter()


@router.get("/listings/", tags=["listing", "view"], response_class=HTMLResponse)
async def read_listings_view(request: Request):
    return templates.TemplateResponse("listings.html", {
        "request": request,
        "title": "Listings",
        "listings": listings_repo.read()
    })


@router.get("/listings/{id}", tags=["listing", "view"], response_class=HTMLResponse)
async def read_listing_view(request: Request, id: str):
    listing = listings_repo.find(id)

    return templates.TemplateResponse("listing.html", {
        "request": request,
        "title": listing.get_title(),
        "listing": listing
    })


@router.post("/api/items/", tags=["listing", "api"])
async def create_listing(title: str = Form(...), price: int = Form(...),
                         description: str = Form(...), pictures: List[str] = Form(...)):

    listing = Listing(title, price, description, pictures)

    listings_repo.create(listing)