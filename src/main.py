#   This is just a...
#    _____  _____   ____ _______ ____ _________     _______  ______
#   |  __ \|  __ \ / __ \__   __/ __ \__   __\ \   / /  __ \|  ____|
#   | |__) | |__) | |  | | | | | |  | | | |   \ \_/ /| |__) | |__
#   |  ___/|  _  /| |  | | | | | |  | | | |    \   / |  ___/|  __|
#   | |    | | \ \| |__| | | | | |__| | | |     | |  | |    | |____
#   |_|    |_|  \_\\____/  |_|  \____/  |_|     |_|  |_|    |______|
#
#   ...written with love in Python <3
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
from pysondb import db
from .routers import items, bids, users

users_db = db.getDb("data/users.json")

templates = Jinja2Templates(directory="src/templates")

app = FastAPI()

app.mount("/static", StaticFiles(directory="src/static"), name="static")

app.include_router(items.router)
app.include_router(bids.router)
app.include_router(users.router)


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
