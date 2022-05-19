from fastapi import FastAPI
from starlette.status import HTTP_200_OK

from items_views import router as items_router
from models_views import router as models_router
from users.api import router as users_router

app = FastAPI()
app.include_router(items_router)
app.include_router(users_router)
app.include_router(models_router)


@app.get("/")
def root():
    """
    :return:
    """
    return {"message": "Hello, World!"}


@app.get("/ping/", status_code=HTTP_200_OK)
def ping():
    """

    :return:
    """
    return {"message": "pong"}
