from fastapi import FastAPI

from . import models
from .routes import routers
from .database import Base, engine

app = FastAPI()
Base.metadata.create_all(bind=engine)

for router in routers:
    app.include_router(router)

@app.get("/")
def root():
    return {"message": "CS2 bot API"}

"""
MESSAGE TO TOMMORROW ME:
 - go back to pipeline, start extracting match data
 - refactor link-steam 
 - start putting the posts in postgres_loader
"""