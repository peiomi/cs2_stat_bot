from .player_routes import router as player_router
from .match_routes import router as match_router
from .player_stats_routes import router as stats_router
from .guild_routes import router as guild_router
from .round_routes import router as round_router
from .map_routes import router as map_router
from .discord_user_routes import router as discord_user_router
from .kill_event_routes import router as kill_event_router
from .grenade_event_routes import router as grenade_event_router

routers = [
    player_router,
    match_router,
    stats_router,
    guild_router,
    round_router,
    map_router,
    discord_user_router,
    kill_event_router,
    grenade_event_router
]