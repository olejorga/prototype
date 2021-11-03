from typing import List
from fastapi import APIRouter, Request, Form
from fastapi.param_functions import Depends
from fastapi.responses import HTMLResponse
from fastapi.exceptions import HTTPException
from ..dependencies import get_templates, get_repositories
from ...core.entities.listing import Listing


router = APIRouter()


@router.get("/listings/", tags=["listing", "view"], response_class=HTMLResponse)
async def read_listings_view(request: Request, templates = Depends(get_templates), 
                             repos = Depends(get_repositories)):
    
    return templates.TemplateResponse("listings.html", {
        "request": request,
        "title": "Annonser",
        "listings": repos["listings"].read()
    })


@router.get("/listings/my", tags=["listing", "view"], response_class=HTMLResponse)
async def read_sellers_listings_view(request: Request, templates = Depends(get_templates), 
                                     repos = Depends(get_repositories)):
    
    user = request.state.current_user

    if user is None or user.get_class_name() != "Seller":
        raise HTTPException(status_code = 403)
    
    return templates.TemplateResponse("listings.html", {
        "request": request,
        "title": "Mine annonser",
        "listings": repos["listings"].search("user_id", user.id)
    })


@router.get("/listings/new", tags=["listing", "view"], response_class=HTMLResponse)
async def read_new_listing_view(request: Request, templates = Depends(get_templates)):
    user = request.state.current_user

    if user is None or user.get_class_name() != "Seller":
        raise HTTPException(status_code = 403)
    
    return templates.TemplateResponse("new_listing.html", {
        "request": request,
        "title": "Ny annonse"
    })


@router.get("/listings/{id}", tags=["listing", "view"], response_class=HTMLResponse)
async def read_listing_view(request: Request, id: str, templates = Depends(get_templates), 
                            repos = Depends(get_repositories)):
    
    listing = repos["listings"].find(id)

    return templates.TemplateResponse("listing.html", {
        "request": request,
        "title": listing.get_title(),
        "listing": listing
    })


@router.post("/api/listings/", tags=["listing", "api"])
async def create_listing(request: Request, title: str = Form(...), price: int = Form(...),
                         description: str = Form(...), pictures: List[str] = Form(...),
                         repos=Depends(get_repositories)):

    if request.state.current_user.get_class_name() != "Seller":
        raise HTTPException(status_code=403)

    listing = Listing(title, price, description, pictures, request.state.current_user.id)

    repos["listings"].create(listing)
