from fastapi import Header, HTTPException
from starlette.status import HTTP_401_UNAUTHORIZED

from . import crud
from .models import UserOut


def get_user_by_auth_token(
    token: str = Header(..., description="user auth token")
) -> UserOut:
    user_in_db = crud.get_user_by_token(token)
    if user_in_db:
        user = crud.read_user(user_in_db.id)
        if user:
            return user

    raise HTTPException(
        status_code=HTTP_401_UNAUTHORIZED, detail={"message": "Invalid token!"}
    )
