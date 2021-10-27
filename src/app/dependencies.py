from functools import lru_cache
from fastapi import Request, Depends
from fastapi.templating import Jinja2Templates
from .models.pickle_repository import PickleRepository


@lru_cache # Cache repo instances, to reduse resource usage
def get_repositories():
    return {
        "listings": PickleRepository("data/listings.dat"),
        "users": PickleRepository("data/users.dat")
    }


@lru_cache # Cache template instance, to reduse resource usage
def get_templates():
    return Jinja2Templates(directory="src/app/templates")


async def get_current_user(request: Request, repos = Depends(get_repositories)):
    user_token = request.cookies.get("user_token")
    request.state.current_user = repos["users"].find(user_token)