class Bid:

    def __init__(self, listing_id: int, user_id: int, amount: int):

        self.set_listing_id(listing_id)
        self.set_user_id(user_id)
        self.set_amount(amount)


    def get_listing_id(self):
        return self.listing_id


    def set_listing_id(self, new_listing_id: int):
        self.listing_id = new_listing_id


    def get_user_id(self):
        return self.user_id


    def set_user_id(self, new_user_id: int):
        self.user_id = new_user_id

    
    def get_amount(self):
        return self.amount


    def set_amount(self, new_amount: int):
        self.amount = new_amount