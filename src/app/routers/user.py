from fastapi import APIRouter, Form
from fastapi.responses import Response, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.exceptions import HTTPException
from ..models.pickle_repository import PickleRepository


users_repo = PickleRepository("data/users.dat")

templates = Jinja2Templates(directory="src/templates")

router = APIRouter()


@router.post("/api/users/login", tags=["user", "api"])
async def login_user(response: Response, username: str = Form(...), 
                     password: str = Form(...)):

    user = users_repo.search("username", username)[0]

    if user is None or user.password != password:
        raise HTTPException(status_code = 403)
    
    response = RedirectResponse(url="/")
    response.status_code = 302
    response.set_cookie("user_token", user.id)

    return response


@router.get("/api/users/logout", tags=["user", "api"])
async def logout_user(response: Response):
    response = RedirectResponse(url="/")
    response.status_code = 302
    response.delete_cookie("user_token")

    return response