from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..database.util import get_db
from ..models.match import Match
from ..schemas.match_schema import MatchResponse, MatchCreate

router = APIRouter(prefix="/matches", tags=["Matches"])

def get_match_or_404(
    match_id: int,
    db: Session
):

    cs_match = (
        db.query(Match)
        .filter(Match.id == match_id)
        .first()
    )

    if not cs_match:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Match not found"
        )

    return cs_match

@router.get("/", response_model=list[MatchResponse])
def get_matches(db: Session = Depends(get_db)):
    return db.query(Match).all()

@router.get("/{match_id}", response_model=MatchResponse)
def get_match(
    match_id: int,
    db: Session = Depends(get_db)
):
    return get_match_or_404(match_id, db)

@router.post("/", response_model=MatchResponse, status_code=status.HTTP_201_CREATED)
def create_match(
    match: MatchCreate,
    db: Session = Depends(get_db)
):

    existing_match = (
        db.query(Match)
        .filter(Match.demo_filename = match.demo_filename)
        .first()
    )

    if existing_match:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Match already exists"
        )

    new_match = Match(
        map_id=match.map_id,
        match_date=match.match_date,
        demo_filename=match.demo_filename,
        winning_team=match.winning_team
    )

    db.add(new_match)
    db.commit()
    db.refresh(new_match)

    return new_match

@router.delete("/{match_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_match(
    match_id: int,
    db: Session = Depends(get_db)
):
    cs_match = get_match_or_404(match_id, db)

    db.delete(cs_match)
    db.commit()