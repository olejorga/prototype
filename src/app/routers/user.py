from fastapi import APIRouter, Form, Depends
from fastapi.responses import Response, RedirectResponse
from fastapi.exceptions import HTTPException
from ..dependencies import get_repositories


router = APIRouter()


@router.post("/api/users/login", tags=["user", "api"])
async def login_user(response: Response, username: str = Form(...), 
                     password: str = Form(...), repos = Depends(get_repositories)):

    users = repos["users"].search("username", username)

    if users == []:
        user = None
    else:
        user = users[0]

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