from fastapi import APIRouter
from ..database.util import get_db

router = APIRouter(prefix="/players", tags=["Players"])

@router.get("/")
def get_players():
    return { "message": "all players "}