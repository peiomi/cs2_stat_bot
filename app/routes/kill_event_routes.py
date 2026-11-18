from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import or_
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import KillEvent
from ..schemas.kill_event_schema import KillEventCreate, KillEventResponse
from .round_routes import get_round_or_404

router = APIRouter(prefix="/matches/{match_id}/rounds/{round_number}/kill-events", tags=["Kill Events"])

@router.get("/", response_model=list[KillEventResponse])
def get_kill_events(
    match_id: int,
    round_number: int,
    player_id: int,
    db: Session = Depends(get_db)
):

    match_round = get_round_or_404(match_id, round_number, db)

    kill_events = (
        db.query(KillEvent)
        .filter(
            KillEvent.round_id == match_round.id,
            or_(
                KillEvent.victim_id == player_id,
                KillEvent.killer_id == player_id
            )
        )
        .all()
    )

    return kill_events

@router.post("/", response_model=KillEventResponse, status_code=status.HTTP_201_CREATED)
def create_kill_event(
    match_id: int,
    round_number: int,
    kill_event: KillEventCreate,
    db: Session = Depends(get_db)
):

    match_round = get_round_or_404(match_id, round_number, db)

    new_kill_event = KillEvent(
        round_id=match_round.id,
        match_id=match_id,
        killer_id=kill_event.killer_id,
        victim_id=kill_event.victim_id,
        weapon=kill_event.weapon,
        is_headshot=kill_event.is_headshot,
        x=kill_event.x,
        y=kill_event.y,
        z=kill_event.z
    )

    db.add(new_kill_event)
    db.commit()
    db.refresh(new_kill_event)

    return new_kill_event