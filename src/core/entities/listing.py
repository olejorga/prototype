import re
from typing import List
from .entity import Entity


class Listing(Entity):

    def __init__(self, title: str, price: int, description: str, 
                 pictures: List[str], user_id: str):

        self.set_title(title)
        self.set_price(price)
        self.set_description(description)
        self.set_pictures(pictures)


    def get_title(self):
        return self.title


    def set_title(self, new_title: str):
        regex = "[A-Za-z0-9-_\s]{1,}"

        if not re.fullmatch(regex, new_title):
            raise ValueError("Invalid title")

        self.title = new_title


    def get_price(self):
        return self.price


    def set_price(self, new_price: int):
        if new_price <= 0:
            raise ValueError("Invalid price")

        self.price = new_price


    def get_description(self):
        return self.description


    def set_description(self, new_description: str):
        self.description = new_description

    
    def get_pictures(self):
        return self.pictures


    def set_pictures(self, new_pictures: List[str]):
        self.pictures = new_pictures