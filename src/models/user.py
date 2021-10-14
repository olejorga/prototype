from pydantic import BaseModel, validator


ROLES = ["END_USER", "PLATFORM_OWNER", "SELLER"]


class User(BaseModel):
    username: str = ""
    first_name: str = ""
    last_name: str = ""
    email_address: str = ""
    phone_number: int = 0
    role: str = ""

    @validator("role")
    def role_must_be_predefined(cls, role):
        if role not in ROLES:
            raise ValueError("Role must be either " + ", ".join(ROLES))
        
        return role
