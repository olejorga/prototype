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

# Importing FastAPI and modules
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

# Importing routers
from .routers import items

# Loading template-html-files
templates = Jinja2Templates(directory="src/templates")

# Initializing FastAPI...
app = FastAPI()

# Host static files
app.mount("/static", StaticFiles(directory="src/static"), name="static")

# Initializing routes...
app.include_router(items.router)


@app.get("/", response_class=HTMLResponse)
async def read_root_view(request: Request):
    return templates.TemplateResponse(
        "index.html", {
            "request": request,
            "title": "Hjem"
        })
