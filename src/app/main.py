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

from fastapi import FastAPI, Request, Cookie
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, Response
from fastapi.templating import Jinja2Templates
from .routers import listing, user, bid, search


templates = Jinja2Templates(directory="src/app/templates")

app = FastAPI()

app.include_router(listing.router)
app.include_router(user.router)
app.include_router(bid.router)
app.include_router(search.router)

from .models.pickle_repository import PickleRepository
from ..core.entities.sale import Sale
from ..core.entities.auction import Auction

listings = PickleRepository("data/listings.dat")

#listings.create(Sale("A thing", 100, "...", ["..."]))
#listings.create(Auction("A thing", 100, "...", ["..."], "2022-10-25 19:17:10.601901"))

"""
@app.get("/", tags=['root view'], response_class=HTMLResponse)
async def read_root_view(request: Request, user_session = Cookie(None)):
    if user_session is None:
        user_session = 0
    
    user = users_db.getBy({"id": int(user_session)})

    if user == []:
        user = None
    else:
        user = user[0]

    return templates.TemplateResponse(
        "index.html", {
            "request": request,
            "title": "Hjem",
            "user": user
        })
"""