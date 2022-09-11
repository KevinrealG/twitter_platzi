#Python
from datetime import date
from uuid import UUID
from typing import Optional

#Pydantic
from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import Field

#FastAPI
class UserBase(BaseModel):
    user_id: UUID = Field(...)
    email: EmailStr = Field(...)

class UserLogin(UserBase):
    password: str = Field(
        ..., 
        min_length=8,
        max_length=128,
    )

class User(UserBase):
    first_name: str = Field(
        ...,
        min_length=1,
        max_length=50
    )
    last_name: str = Field(
        ...,
        min_length=1,
        max_length=50
    )
    birth_date: Optional[date] = Field(default=None)

class UserRegister(User):  # Heredamos de User y PasswordMixin
    password: str = Field(
        ...,
        min_length=8,
        max_length=128,
    )
    class Config:
        schema_extra = {
            "example": {
                "user_id": "f4a4c3b0-5b6c-4b4a-9c1c-1c1c1c1c1c1c",
                "email": "k12233ml@gmail.com",
                "password": "12345678",
                "first_name": "Kev",
                "last_name": "M",
                "birth_date": "1995-01-01"
            }
        }