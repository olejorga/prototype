from pydantic import BaseModel
from datetime import datetime


class Item(BaseModel):
    name: str = ""
    price: int = 0
    description: str = ""
    pictures: list = [""]
    auction_time: datetime = datetime.now()
    is_auction: int = 0
