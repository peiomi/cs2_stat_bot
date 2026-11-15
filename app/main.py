from fastapi import FastAPI

from .database.connection import Base, engine
from .routes.player_routes import router as player_router
from .routes.match_routes import router as match_router
from .routes.player_stats_routes import router as stats_router

app = FastAPI()
Base.metadata.create_all(bind=engine)

app.include_router(player_router)
app.include_router(match_router)
app.include_router(stats_router)

@app.get("/")
def root():
    return {"message": "CS2 bot API"}

"""
MESSAGE TO TOMMORROW ME:
 - routes 
 - dont leave pc until routes r routing 
"""