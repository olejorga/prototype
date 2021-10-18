from pydantic import BaseModel


class Bid(BaseModel):
    bid_value: int = 0
    item_id: int = 0
    user_id: int = 0
