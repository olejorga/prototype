from pydantic import BaseModel


class Item(BaseModel):
    name: str = ""
    price: int = 0
    description: str = ""
    pictures: list[str] = [""]
