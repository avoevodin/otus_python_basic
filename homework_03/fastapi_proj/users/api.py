from fastapi import APIRouter, status, Depends
from starlette.status import HTTP_404_NOT_FOUND

from . import crud
from .dependencies import get_user_by_auth_token
from .models import UserIn, UserOut

router = APIRouter(tags=["Users"], prefix="/users")


@router.get("", response_model=list[UserOut])
def list_users():
    """

    :return:
    """
    return crud.list_users()


@router.get("/me", response_model=UserOut)
def read_user_me(user: UserIn = Depends(get_user_by_auth_token)):
    """

    :return:
    """
    return user


@router.get(
    "/{user_id}",
    response_model=UserOut,
    responses={
        HTTP_404_NOT_FOUND: {
            "description": "User not found",
            "content": {
                "application/json": {
                    "schema": {
                        "title": "Not Found",
                        "type": "object",
                        "properties": {
                            "detail": {
                                "title": "Detail",
                                "type": "string",
                                "example": "user #0 not found",
                            },
                        },
                    },
                }
            },
        },
    },
)
def read_user(user_id: int):
    """

    :param user_id:
    :return:
    """
    return crud.read_user(user_id)


@router.post(
    "",
    response_model=UserOut,
    response_model_exclude_unset=True,
    status_code=status.HTTP_201_CREATED,
)
def create_user(user: UserIn):
    """

    :param user:
    :return:
    """
    return crud.create_user(user)
