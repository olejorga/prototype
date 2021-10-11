from pydantic import BaseModel


class Receipt(BaseModel):
    id: int = 0
    date: datetime.date = 0
    product_name: str = ""
    price: int = 0
