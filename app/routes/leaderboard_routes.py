from sqlalchemy.orm import Session
from ..database.util import get_db

router = APIRouter(prefix="/", tags=[""])

""" 
GET /guilds/{guild_id}/leaderboard
GET /guilds/{guild_id}/leaderboard/kd
GET /guilds/{guild_id}/leaderboard/winrate
GET /guilds/{guild_id}/leaderboard/hs 
"""