import datetime
from typing import List
from .listing import Listing


class Auction(Listing):

    def __init__(self, title: str, price: int, description: str, 
                 pictures: List[str], end_datetime: str):

        super().__init__(title, price, description, pictures)

        self.set_end_datetime(end_datetime)


    def get_end_datetime(self):
        return self.end_datetime


    def set_end_datetime(self, new_end_datetime: str):
        format = "%Y-%m-%d %H:%M:%S.%f"

        try:
            datetime.datetime.strptime(new_end_datetime, format)
        except:
            raise ValueError("Invalid end datetime string")

        self.end_datetime = new_end_datetime