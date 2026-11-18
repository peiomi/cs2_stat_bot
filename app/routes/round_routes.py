from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..database.util import get_db
from ..models.round import Round
from ..schemas.round_schema import RoundCreate, RoundResponse
from .match_routes import get_match_or_404

router = APIRouter(prefix="/matches/{match_id}/rounds", tags=["Rounds"])

def get_round_or_404(
    match_id: int,
    round_number: int,
    db: Session
):

    match_round = (
        db.query(Round)
        .filter(
            Round.match_id == match_id,
            Round.round_number == round_number
        )   
        .first()
    )

    if not match_round:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Round not found"
        )

    return match_round

@router.get("/", response_model=list[RoundResponse])
def get_rounds(
    match_id: int,
    db: Session = Depends(get_db)
):
    get_match_or_404(match_id, db)
    
    rounds = (
        db.query(Round)
        .filter(Round.match_id == match_id)
        .all()
    )

    return rounds

@router.get("/{round_number}", response_model=RoundResponse)
def get_round(
    match_id: int,
    round_number: int,
    db: Session = Depends(get_db)
):

    return get_round_or_404(match_id, round_number, db)

@router.post("/", response_model=RoundResponse, status_code=status.HTTP_201_CREATED)
def create_round(
    match_id: int,
    match_round: RoundCreate,
    db: Session = Depends(get_db),
):

    get_match_or_404(match_id, db)

    existing_round = (
        db.query(Round)
        .filter(
            Round.match_id == match_id,
            Round.round_number == match_round.round_number
        )
        .first()
    )

    if existing_round:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Round already exists"
        )

    new_round = Round(
        match_id=match_id,
        round_number=match_round.round_number,
        winning_side=match_round.winning_side
    )

    db.add(new_round)
    db.commit()
    db.refresh(new_round)

    return new_round