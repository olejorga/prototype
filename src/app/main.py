#
#   This is just a...
#  _______________________________________________________________________________________
#      ____      ____        __    ______      __    ______    _     _    ____      _____ 
#      /    )    /    )    /    )    /       /    )    /       |    /     /    )    /    '
#  ---/____/----/___ /----/----/----/-------/----/----/--------|---/-----/____/----/__----
#    /         /    |    /    /    /       /    /    /         |  /     /         /       
#  _/_________/_____|___(____/____/_______(____/____/__________|_/_____/_________/____ ___
#                                                               /                         
#   ...written with love in Python <3                       (_ /                          
#
#   Made by:
#       * Erik Teien Jarem
#       * Mujibullah Rahimi
#       * Ole-Jørgen Andersen
#       * Simen Jacobsen Øygard
#       * Sivert Østgård
#

from os import environ
from fastapi import FastAPI, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from .routers import listing, user, search
from .models.pickle_repository import PickleRepository


async def get_current_user(request: Request):
    user_token = request.cookies.get("user_token")
    request.state.current_user = users_repo.find(user_token)


users_repo = PickleRepository(environ["USERS_REPO_PATH"])

templates = Jinja2Templates(directory="src/app/templates")

app = FastAPI(dependencies=[Depends(get_current_user)])

app.include_router(listing.router)
app.include_router(user.router)
app.include_router(search.router)


@app.get("/", tags=["root", "view"], response_class=HTMLResponse)
async def read_root_view(request: Request):
    return templates.TemplateResponse(
        "index.html", {
            "request": request,
            "title": "Hjem"
        })