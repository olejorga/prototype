from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse
from ..dependencies import get_templates, get_repositories


router = APIRouter()


@router.get("/search", tags=["search", "view"], response_class=HTMLResponse)
async def read_search_view(request: Request, input: str, templates = Depends(get_templates), 
                           repos = Depends(get_repositories)):

    return templates.TemplateResponse("listings.html", {
        "request": request,
        "title": "Søkeresultater", 
        "listings": repos["listings"].search("title", input)
    })
