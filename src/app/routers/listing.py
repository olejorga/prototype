from os import environ
from typing import List
from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.exceptions import HTTPException
from ...core.entities.listing import Listing
from ..models.pickle_repository import PickleRepository


listings_repo = PickleRepository(environ["LISTINGS_REPO_PATH"])
users_repo = PickleRepository(environ["USERS_REPO_PATH"])

templates = Jinja2Templates(directory=environ["TEMPLATES_PATH"])

router = APIRouter()


@router.get("/listings/", tags=["listing", "view"], response_class=HTMLResponse)
async def read_listings_view(request: Request):
    return templates.TemplateResponse("listings.html", {
        "request": request,
        "title": "Annonser",
        "listings": listings_repo.read()
    })


@router.get("/listings/my", tags=["listing", "view"], response_class=HTMLResponse)
async def read_sellers_listings_view(request: Request):
    user = request.state.current_user

    if user is None or user.get_class_name() != "Seller":
        raise HTTPException(status_code = 403)
    
    return templates.TemplateResponse("listings.html", {
        "request": request,
        "title": "Mine annonser",
        "listings": listings_repo.search("user_id", user.id)
    })


@router.get("/listings/new", tags=["listing", "view"], response_class=HTMLResponse)
async def read_new_listing_view(request: Request):
    user = request.state.current_user

    if user is None or user.get_class_name() != "Seller":
        raise HTTPException(status_code = 403)
    
    return templates.TemplateResponse("new_listing.html", {
        "request": request,
        "title": "Ny annonse"
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