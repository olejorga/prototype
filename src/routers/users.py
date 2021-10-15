from fastapi import APIRouter, Request, Form, status, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import HTMLResponse, Response, RedirectResponse
from fastapi.templating import Jinja2Templates
from pysondb import db
from ..models.user import User

users_db = db.getDb("data/users.json")

templates = Jinja2Templates(directory="src/templates")

router = APIRouter()


@router.post("/api/users/login", tags=['users api'])
async def login_user(response: Response, username: str = Form(...), password: str = Form(...)):
    user = users_db.getBy({"username": username})[0]

    if user is None or user["password"] != password:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, 
                            detail="Feil brukernavn eller passord")
    else:
        token = user["id"]
        response = RedirectResponse(url="/")
        response.status_code = 302
        response.set_cookie("user_session", token)

        return response


@router.get("/api/users/logout", tags=['users api'])
async def logout_user(response: Response):
    response = RedirectResponse(url="/")
    response.status_code = 302
    response.delete_cookie("user_session")

    return response
        

@router.post("/api/users/", tags=['users api'])
async def create_user(user: User):
    id = users_db.add(jsonable_encoder(user))
    return id  


#   @router.get("/items/{id}", tags=['items view'], response_class=HTMLResponse)
#   async def read_item_view(id: int, request: Request):
#       return templates.TemplateResponse(
#           "item.html", {
#               "request": request,
#               "title": "Item",
#              "item": items_db.getBy({"id": id})[0]
#          })