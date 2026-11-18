from fastapi import FastAPI

from . import models
from .routes import routers
from .database.connection import Base, engine

app = FastAPI()
Base.metadata.create_all(bind=engine)

for router in routers:
    app.include_router(router)

@app.get("/")
def root():
    return {"message": "CS2 bot API"}

"""
MESSAGE TO TOMMORROW ME:
 - decide between demoparser2 or awpy
"""