from fastapi import FastAPI
from items_views import router as items_router
from users.api import router as users_router
from models_views import router as models_router

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
