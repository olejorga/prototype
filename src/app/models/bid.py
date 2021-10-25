from pydantic import BaseModel


class Bid(BaseModel):
    bid_value: int = 0
    item_id: int = 0
    user_id: int = 0

    def __init__(self, bid_value: int, item_id: int, user_id: int, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bid_value = bid_value
        self.item_id = item_id
        self.user_id = user_id

    def get_bid_value(self):
        return self.bid_value

    def get_item_id(self):
        return self.item_id

    def get_user_id(self):
        return self.user_id

    def set_bid_value(self, new_bid_value: int):
        self.bid_value = new_bid_value

    def set_item_id(self, new_item_id: int):
        self.item_id = new_item_id

    def set_user_id(self, new_user_id):
        self.user_id = new_user_id


class UpdateBid(BaseModel):
    bid_value: int = None
    user_id: int = None

    def __init__(self, bid_value: int, user_id: int, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bid_value = bid_value
        self.user_id = user_id

    def get_bid_value(self):
        return self.bid_value

    def get_user_id(self):
        return self.user_id
