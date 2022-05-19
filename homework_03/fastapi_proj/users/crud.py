from typing import Optional

from .models import UserIn, UserInDB, UserOut

USER_ID_TO_USER: dict[int, UserOut] = {}
USER_TOKEN_TO_USER: dict[str, UserInDB] = {}


def list_users():
    """

    :return:
    """
    return list(USER_ID_TO_USER.values())


def read_user(user_id: int) -> Optional[UserOut]:
    """

    :param user_id:
    :return:
    """
    return USER_ID_TO_USER.get(user_id)


def create_user(user: UserIn) -> Optional[UserOut]:
    """

    :param user:
    :return:
    """
    user_saved = fake_save_user(user)
    return user_saved


def get_user_by_token(token: str) -> Optional[UserInDB]:
    """

    :param token:
    :return:
    """
    return USER_TOKEN_TO_USER.get(token)


def fake_save_user(user: UserIn):
    """

    :param user:
    :return:
    """
    hashed_password = fake_password_hasher(user.password)
    new_id = len(USER_ID_TO_USER) + 1
    user_out = UserOut(id=new_id, **user.dict())
    user_in_db = UserInDB(**user_out.dict(), hashed_password=hashed_password)
    user_in_db.id = new_id
    print(user_in_db.dict())

    USER_ID_TO_USER.update({user_out.id: user_out})
    USER_TOKEN_TO_USER.update({user_in_db.token: user_in_db})
    print(user_in_db.dict())
    return user_out


def fake_password_hasher(raw_password: str):
    return "supersecret" + raw_password
