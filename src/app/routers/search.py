from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse
from ..dependencies import get_templates, get_repositories


router = APIRouter()


@router.get("/search", tags=["search", "view"], response_class=HTMLResponse)
async def read_search_view(request: Request, input: str, templates = Depends(get_templates), 
                           repos = Depends(get_repositories)):

    result = []

    for listing in repos["listings"].entities:
        if input.lower() in listing.title.lower():
            result.append(listing)

    if not result: # If no results on title search
        for listing in repos["listings"].entities:
            if input.lower() in listing.description.lower():
                result.append(listing)

    return templates.TemplateResponse("listings.html", {
        "request": request,
        "title": "Søkeresultater", 
        "listings": result
    })
