from pydantic import BaseModel


class Item(BaseModel):
    name: str = ""
    price: float = 0.0
    description: str = ""
    pictures: list[str] = [""]
