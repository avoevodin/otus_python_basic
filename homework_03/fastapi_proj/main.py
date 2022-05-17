from enum import Enum

from fastapi import FastAPI


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


app = FastAPI()


@app.get("/")
def root():
    """
    :return:
    """
    return {"message": "Hello, World!"}


@app.get("/items/{item_id}")
def root(item_id: int):
    """

    :param item_id:
    :return:
    """
    return {"item_id": item_id}


@app.get("/users/me")
def read_user_me():
    """

    :return:
    """
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
def read_user(user_id: str):
    return {"user_id": user_id}


@app.get("/models/{model_name}")
def get_model(model_name: ModelName):
    """

    :param model_name:
    :return:
    """
    if model_name == ModelName.alexnet:
        message = "Deep learning FTW!"
    elif model_name.value == "lenet":
        message = "LeCNN all the images"
    else:
        message = "Have some residuals"

    return {"model_name": model_name, "message": message}
