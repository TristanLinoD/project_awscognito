from typing import Annotated
from annotated_types import MinLen, MaxLen
from pydantic import BaseModel, EmailStr, Field

class UserSignup(BaseModel):
    full_name: str = Field(max_length=50)
    email: EmailStr
    phone_number: Annotated[str, MinLen(10)]
    password: Annotated[str, MinLen(8)]
    role: str

class UserVerify(BaseModel):
    email: EmailStr
    confirmation_code: Annotated[str, MaxLen(6)]

class UserSignin(BaseModel):
    email: EmailStr
    password: Annotated[str, MinLen(8)]
