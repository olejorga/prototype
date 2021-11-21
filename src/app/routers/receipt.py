from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse, Response, RedirectResponse
from fastapi.exceptions import HTTPException
from ..dependencies import get_templates, get_repositories
from ...core.entities.receipt import Receipt


router = APIRouter()


@router.get("/receipts/", tags=["receipt", "view"], response_class=HTMLResponse)
async def read_receipt_view(request: Request, templates = Depends(get_templates), 
                            repos = Depends(get_repositories)):

    user = request.state.current_user
    
    if user is None or user.get_class_name() == "Admin":
        raise HTTPException(status_code=403)

    return templates.TemplateResponse("receipts.html", {
        "request": request,
        "title": "Kvittering",
        "receipts": repos["receipts"].search("user_id", user.id)
    })


@router.get("/receipts/{id}", tags=["receipt", "view"], response_class=HTMLResponse)
async def read_receipt(request: Request, id: str, templates = Depends(get_templates), 
                       repos = Depends(get_repositories)):

    return templates.TemplateResponse("receipt.html",{
        "request": request,
        "title": "Kvittering",
        "receipt": repos["receipts"].find(id)
    })


@router.get("/api/receipts/{id}", tags=["receipt", "api"])
async def create_receipt(response: Response, request: Request, id: str,
                         repos = Depends(get_repositories)):

    user = request.state.current_user

    if user is None or user.get_class_name() != "Buyer":
        raise HTTPException(status_code = 403)
    
    listing = repos["listings"].find(id)
    receipt = Receipt(listing, user.id)
    repos["receipts"].create(receipt)

    listing = repos["listings"].delete(id)

    response = RedirectResponse(url="/receipts/")
    response.status_code = 302
    
    return response


@router.post("/api/checkout/{id}", tags=["receipt", "api"])
async def goto_checkout(response: Response, request: Request, id: str):

    user = request.state.current_user

    if user is None or user.get_class_name() != "Buyer":
        raise HTTPException(status_code = 403)
    
    # PAYMENT HANDLER CODE

    response = RedirectResponse(url="/api/receipts/"+id)
    response.status_code = 302
    
    return response


@router.delete("/api/receipts/", tags=["receipt", "api"])
async def delete_receipt(request: Request, id: str, repos=Depends(get_repositories)):

    if request.state.current_user.get_class_name() != "Admin":
        raise HTTPException(status_code=403)

    repos["receipts"].delete(id)