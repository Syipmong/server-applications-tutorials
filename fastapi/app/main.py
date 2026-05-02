from fastapi import FastAPI

from app.routers.users import router as users_router
from app import models
from app.database import engine


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users_router)

@app.get('/')
def read_root():
    return {'message':'Hello World'}
