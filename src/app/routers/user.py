from fastapi import APIRouter, Request, Form, status, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import HTMLResponse, Response, RedirectResponse
from fastapi.templating import Jinja2Templates
from ...core.entities.buyer import Buyer
from ..models.pickle_repository import PickleRepository


users_repo = PickleRepository("data/users.dat")

templates = Jinja2Templates(directory="src/templates")

router = APIRouter()


@router.post("/api/users/login", tags=["user", "api"])
async def login_user(response: Response, username: str = Form(...), 
                     password: str = Form(...)):

    user = users_repo.search("username", username)

    if len(user) == 1 and user[0].password == password:
        token = user["id"]
        response = RedirectResponse(url="/")
        response.status_code = 302
        response.set_cookie("user_token", token)

        return response


@router.get("/api/users/logout", tags=["user", "api"])
async def logout_user(response: Response):
    response = RedirectResponse(url="/")
    response.status_code = 302
    response.delete_cookie("user_token")

    return response