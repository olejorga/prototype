from .user import User


class Seller(User):

    def __init__(self, username: str, password: str, email_address: str,
                 phone_number: str, company_name: str):

        super().__init__(username, password, email_address, phone_number)

        self.set_company_name(company_name)


    def get_company_name(self):
        return self.company_name


    def set_company_name(self, new_company_name: str):
        self.company_name = new_company_name