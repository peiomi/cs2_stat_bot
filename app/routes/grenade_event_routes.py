from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import GrenadeEvent
from ..schemas.grenade_event_schema import GrenadeEventResponse, GrenadeEventCreate
from .round_routes import get_round_or_404

router = APIRouter(prefix="/matches/{match_id}/rounds/{round_number}/grenade-events", tags=["Grenade Events"])

@router.get("/", response_model=list[GrenadeEventResponse])
def get_grenade_events(
    match_id: int,
    round_number: int,
    player_id: int,
    db: Session = Depends(get_db)
):

    match_round = get_round_or_404(match_id, round_number, db)

    grenade_events = (
        db.query(GrenadeEvent)
        .filter(
            GrenadeEvent.round_id == match_round.id,
            GrenadeEvent.player_id == player_id
            )
        .all()
    )

    return grenade_events

@router.post("/", response_model=GrenadeEventResponse, status_code=status.HTTP_201_CREATED)
def create_grenade_event(
    match_id: int,
    round_number: int,
    grenade_event: GrenadeEventCreate,
    db: Session = Depends(get_db)
):

    match_round = get_round_or_404(match_id, round_number, db)

    new_grenade_event = GrenadeEvent(
        round_id=match_round.id,
        match_id=match_id,
        player_id=grenade_event.player_id,
        grenade_type=grenade_event.grenade_type,
        damage=grenade_event.damage,
        blind_time=grenade_event.blind_time,
        x=grenade_event.x,
        y=grenade_event.y,
        z=grenade_event.z
    )

    db.add(new_grenade_event)
    db.commit()
    db.refresh(new_grenade_event)

    return new_grenade_event