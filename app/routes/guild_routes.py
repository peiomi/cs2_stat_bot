from sqlalchemy.orm import Session
from ..database.util import get_db

router = APIRouter(prefix="/", tags=[""])

""" GET    /guilds
GET    /guilds/{id}
POST   /guilds
PUT    /guilds/{id} """