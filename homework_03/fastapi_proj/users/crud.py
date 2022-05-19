from models import UserIn


def read_user_me():
    """

    :return:
    """
    return {"user_id": "the current user"}


def read_user(user_id: str):
    """

    :param user_id:
    :return:
    """
    return {"user_id": user_id}


def create_user(user: UserIn):
    """

    :param user:
    :return:
    """
    return user
