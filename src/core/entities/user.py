import re
from .entity import Entity


class User(Entity):

    def __init__(self, username: str, password: str, email_address: str,
                 phone_number: str):

        self.set_username(username)
        self.set_password(password)
        self.set_email_address(email_address)
        self.set_phone_number(phone_number)


    def get_username(self):
        return self.username


    def set_username(self, new_username: str):
        regex = "[A-Za-z0-9-_]{1,}"

        if not re.fullmatch(regex, new_username):
            raise ValueError("Invalid username")

        self.username = new_username


    def get_password(self):
        return self.password


    def set_password(self, new_password: str):
        regex = "[A-Za-z0-9@#$%^&+=-_]{8,}"

        if not re.fullmatch(regex, new_password):
            raise ValueError("Invalid password")

        self.password = new_password


    def get_email_address(self):
        return self.email_address


    def set_email_address(self, new_email_address: str):
        regex = "[^@]+@[^@]+\.[^@]+"

        if not re.fullmatch(regex, new_email_address):
            raise ValueError("Invalid email address")

        self.email_address = new_email_address


    def get_phone_number(self):
        return self.phone_number


    def set_phone_number(self, new_phone_number: str):
        regex = "^[0-9]{8}$"

        if not re.fullmatch(regex, new_phone_number):
            raise ValueError("Invalid phone number")

        self.phone_number = new_phone_number