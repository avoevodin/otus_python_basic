from typing import Union
from uuid import uuid4

from pydantic import BaseModel, EmailStr, Field


class UserBase(BaseModel):
    username: str
    email: EmailStr
    fullname: Union[str, None] = None
    hobbies: list[str] = []


class UserIn(UserBase):
    password: str


class UserOut(UserBase):
    id: int = Field(..., example=123)


def generate_token():
    """

    :return:
    """
    token = str(uuid4())
    return token


class UserInDB(UserOut):
    hashed_password: str
    token: str = Field(default_factory=generate_token)
