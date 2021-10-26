#
#   This is just a...
#  _______________________________________________________________________________
#      ____     ____       __   ______     __   ______   _     _   ____     _____ 
#      /    )   /    )   /    )   /      /    )   /      |    /    /    )   /    '
#  ---/____/---/___ /---/----/---/------/----/---/-------|---/----/____/---/__----
#    /        /    |   /    /   /      /    /   /        |  /    /        /       
#  _/________/_____|__(____/___/______(____/___/_________|_/____/________/____ ___
#                                                        /                       
#   ...written with love in Python <3                (_ /  
#
#   Made by:
#       * Erik Teien Jarem
#       * Mujibullah Rahimi
#       * Ole-Jørgen Andersen
#       * Simen Jacobsen Øygard
#       * Sivert Østgård
#

#from configparser import ConfigParser
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from .routers import listing, user, search
from .models.pickle_repository import PickleRepository


class Main:

    def __init__(self, config):
        
        pass


#config = ConfigParser()
#config.read('config.ini')

users_repo = PickleRepository("data/users.dat")

templates = Jinja2Templates(directory="src/app/templates")

app = FastAPI()

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

"""
@app.middleware("http")
async def set_current_user(request: Request, call_next):
    user_token = request.cookies.get("user_token")

    request.state.current_user = users_repo.find(user_token)

    response = await call_next(request)

    return response
"""