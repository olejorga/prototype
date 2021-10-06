from pydantic import BaseModel
from datetime import datetime, timedelta

def countdown(auction_date: datetime):
    current_date = datetime.now()

    count = int((auction_date - current_date).total_seconds)

    days_remaining = count // 86400
    hours_remaining = (count-days_remaining * 86400) // 3600
    minutes_remaining = (count - days_remaining * 86400 - hours_remaining * 3600) // 60
    seconds_remaining = count - days_remaining * 86400 - hours_remaining * 3600 - minutes_remaining * 60

    string_output = ("{} days, {} hours, {} minutes and {} seconds left of the auction".format(days_remaining, hours_remaining, minutes_remaining, seconds_remaining))
    
    return string_output
      

class Item(BaseModel):
    name: str = ""
    price: int = 0
    description: str = ""
    pictures: list[str] = [""]
    auction_time: datetime = 0



