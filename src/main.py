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

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from .routers import items

templates = Jinja2Templates(directory="src/templates")

app = FastAPI()

app.mount("/static", StaticFiles(directory="src/static"), name="static")

app.include_router(items.router)


@app.get("/", tags=['root view'], response_class=HTMLResponse)
async def read_root_view(request: Request):
    return templates.TemplateResponse(
        "index.html", {
            "request": request,
            "title": "Hjem"
        })
