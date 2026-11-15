from sqlalchemy.orm import Session
from ..database.util import get_db

router = APIRouter(prefix="/demos", tags=[""])

@router.post("/")
@router.get("/")
@router.get("/{id}")