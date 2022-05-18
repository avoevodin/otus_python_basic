from fastapi import APIRouter

router = APIRouter(tags=["Users"], prefix="/users")


@router.get("/me")
def read_user_me():
    """

    :return:
    """
    return {"user_id": "the current user"}


@router.get("/{user_id}")
def read_user(user_id: str):
    return {"user_id": user_id}
