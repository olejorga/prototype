from pydantic import BaseModel
from datetime import timedelta


class Item(BaseModel):
    name: str = ""
    price: int = 0
    description: str = ""
    pictures: list[str] = [""]
    auction_time: timedelta = timedelta(days=0)
