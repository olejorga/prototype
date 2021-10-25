from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from ..models.pickle_repository import PickleRepository


listings_repo = PickleRepository("data/listings.dat")

templates = Jinja2Templates(directory="src/app/templates")

router = APIRouter()


@router.get("/search", tags=["search", "view"], response_class=HTMLResponse)
async def read_search_view(request: Request, input: str):
    listings = listings_repo.search("title", input)

    return templates.TemplateResponse("listings.html", {
        "request": request,
        "title": "Søkeresultater", 
        "listings": listings
    })
