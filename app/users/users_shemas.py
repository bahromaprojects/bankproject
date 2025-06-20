from pydantic import BaseModel, Field


class InsertUser(BaseModel):
    user_name: str
    user_phone_number: str
    user_email: str
