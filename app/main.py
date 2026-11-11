from fastapi import FastAPI, Depends
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from .database.connection import Base, engine
from .routes.player_routes import router as player_router

app = FastAPI()
Base.metadata.create_all(bind=engine)

app.include_router(player_router)

@app.get("/")
def root():
    return {"message": "CS2 bot API"}

"""
MESSAGE TO TOMMORROW ME:
 - finish models/schemas/routes 
 - dont leave pc until routes r routing 
"""