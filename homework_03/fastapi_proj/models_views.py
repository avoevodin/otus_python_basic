from enum import Enum

from fastapi import APIRouter

router = APIRouter(tags=["Models"], prefix="/models")


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


@router.get("/{model_name}")
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
