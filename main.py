from fastapi import FastAPI

from db import models
from db.database import engine
from routers import address

app = FastAPI()
app.include_router(address.router)

models.Base.metadata.create_all(engine)
