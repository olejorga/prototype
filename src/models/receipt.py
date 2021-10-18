from pydantic import BaseModel
from datetime import datetime


class Receipt(BaseModel):
    id: int = 0
    date: datetime = datetime
    product_name: str = ""
    price: int = 0
