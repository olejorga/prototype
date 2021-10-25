from typing import List
from .listing import Listing


class Sale(Listing):
    
    def __init__(self, title: str, price: int, description: str, 
                 pictures: List[str]):

        super().__init__(title, price, description, pictures)