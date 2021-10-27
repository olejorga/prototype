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

from fastapi import FastAPI, Request, Depends
from fastapi.responses import HTMLResponse
from .routers import listing, user, search, receipt
from .dependencies import get_current_user, get_templates


app = FastAPI(dependencies=[Depends(get_current_user)])

app.include_router(listing.router)
app.include_router(user.router)
app.include_router(search.router)
app.include_router(receipt.router)


@app.get("/", tags=["root", "view"], response_class=HTMLResponse)
async def read_root_view(request: Request, templates = Depends(get_templates)):
    
    return templates.TemplateResponse(
        "index.html", {
            "request": request,
            "title": "Hjem"
        })