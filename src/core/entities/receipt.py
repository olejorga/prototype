from datetime import datetime
from .entity import Entity
from .listing import Listing

class Receipt(Entity):
    def __init__(self, listing: Listing):
        self.set_title(listing)
        self.set_price(listing)
        self.set_date()

  
    def get_title(self):
        return self.title

    def set_title(self, listing: Listing):
        self.title = listing.get_title()

    def get_price(self):
        return self.price

    def set_price(self, listing: Listing):
        self.price = listing.get_price()
    
    def get_date(self):
        return self.sale_date
    
    def set_date(self):
        self.sale_date = datetime.now().strftime("%d.%m.%Y - %H:%M:%S")
    