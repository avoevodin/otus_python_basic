from fastapi import APIRouter

import crud
from models import UserIn, UserOut

router = APIRouter(tags=["Users"], prefix="/users")


@router.get("/me")
def read_user_me():
    """

    :return:
    """
    return crud.read_user_me()


@router.get("/{user_id}")
def read_user(user_id: str):
    """

    :param user_id:
    :return:
    """
    return crud.read_user(user_id)


@router.post("", response_model=UserOut, response_model_exclude_unset=True)
def create_user(user: UserIn):
    """

    :param user:
    :return:
    """
    return crud.create_user(user)
