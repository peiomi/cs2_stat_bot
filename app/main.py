from fastapi import FastAPI

from . import models
from .database.connection import Base, engine

from .routes.player_routes import router as player_router
from .routes.match_routes import router as match_router
from .routes.player_stats_routes import router as stats_router
from .routes.guild_routes import router as guild_router
from .routes.round_routes import router as round_router
from .routes.map_routes import router as map_router
from .routes.discord_user_routes import router as discord_user_router
from .routes.kill_event_routes import router as kill_event_router
from .routes.grenade_event_routes import router as grenade_event_router

app = FastAPI()
Base.metadata.create_all(bind=engine)

app.include_router(player_router)
app.include_router(match_router)
app.include_router(stats_router)
app.include_router(guild_router)
app.include_router(round_router)
app.include_router(map_router)
app.include_router(discord_user_router)
app.include_router(kill_event_router)
app.include_router(grenade_event_router)

@app.get("/")
def root():
    return {"message": "CS2 bot API"}

"""
MESSAGE TO TOMMORROW ME:
 - 
"""