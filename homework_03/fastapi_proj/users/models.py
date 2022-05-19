from typing import Union

from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    username: str
    email: EmailStr
    fullname: Union[str, None] = None
    hobbies: list[str] = []


class UserIn(UserBase):
    password: str


class UserOut(UserBase):
    pass
