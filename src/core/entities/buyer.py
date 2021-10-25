from .user import User


class Buyer(User):

    def __init__(self, username: str, password: str, email_address: str,
                 phone_number: str, first_name: str, last_name: str):

        super().__init__(username, password, email_address, phone_number)

        self.set_first_name(first_name)
        self.set_last_name(last_name)


    def get_first_name(self):
        return self.first_name


    def set_first_name(self, new_first_name: str):
        self.first_name = new_first_name


    def get_last_name(self):
        return self.last_name


    def set_last_name(self, new_last_name: str):
        self.last_name = new_last_name