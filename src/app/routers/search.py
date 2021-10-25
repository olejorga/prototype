from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from pysondb import db

items_db = db.getDb("data/items.json")
users_db = db.getDb("data/users.json")

templates = Jinja2Templates(directory="src/templates")

router = APIRouter()


@router.get("/search_result", tags=["Search results"], response_class=HTMLResponse)
async def show_results(request: Request, search_input: str):
    items = items_db.getBy({"name": search_input})
    users = users_db.getBy({"first_name": search_input})
    return templates.TemplateResponse("search_result.html", {
        "request": request,
        "title": "Search results", "items": items, "users": users})
