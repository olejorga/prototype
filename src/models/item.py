from pydantic import BaseModel
from datetime import datetime


class Item(BaseModel):
    name: str = ""
    price: int = 0
    description: str = ""
    pictures: list[str] = [""]
    auction_time: datetime = datetime.now()

