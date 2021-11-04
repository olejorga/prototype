from datetime import datetime
from .entity import Entity
from .listing import Listing

class Receipt(Entity):
    def __init__(self, listing: Listing, user_id: str):
        self.set_title(listing.get_title())
        self.set_price(listing.get_price())
        self.set_date(datetime.now().strftime("%d.%m.%Y - %H:%M:%S"))
        self.set_user_id(user_id)

  
    def get_title(self):
        return self.title

    def set_title(self, new_title: str):
        self.title = new_title

    def get_price(self):
        return self.price

    def set_price(self, new_price: int):
        self.price = new_price
    
    def get_date(self):
        return self.sale_date
    
    def set_date(self, new_date: str):
        self.sale_date = new_date

    def get_user_id(self):
        return self.user_id
    
    def set_user_id(self, new_user_id: str):
        self.user_id = new_user_id
    