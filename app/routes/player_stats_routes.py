from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..database.util import get_db
from ..models.player_match_stats import PlayerMatchStats
from ..schemas.player_match_stats_schema import PlayerMatchStatsCreate, PlayerMatchStatsResponse

router = APIRouter(prefix="/player-stats", tags=["PlayerMatchStats"])


def get_stats_or_404(
    stats_id: int,
    db: Session
):

    stats = (
        db.query(PlayerMatchStats)
        .filter(
            PlayerMatchStats.player_id == player_match_stats.player_id,
            PlayerMatchStats.match_id == player_match_stats.match_id
        )
        .first()
    )

    if not stats:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Stats not found"
        )

    return stats


@router.get("/{stats_id}", response_model=PlayerMatchStatsResponse)
def get_stats(
    stats_id: int,
    db: Session = Depends(get_db)
):
    return get_stats_or_404(stats_id, db)

@router.post("/", response_model=PlayerMatchStatsResponse)
def create_player_stats(
    player_match_stats: PlayerMatchStatsCreate,
    db: Session = Depends(get_db)
):

    existing_stats = (
        db.query(PlayerMatchStats)
        .filter(PlayerMatchStats.id == stats_id)
        .first()
    )

    if existing_stats:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Stats already exist"
        )

    new_stats = PlayerMatchStats(
        player_id=player_match_stats.player_id,
        match_id=player_match_stats.match_id,
        kills=player_match_stats.kills,
        deaths=player_match_stats.deaths,
        assists=player_match_stats.assists,
        hs_kills=player_match_stats.hs_kills,
        adr=player_match_stats.adr,
        rating=player_match_stats.rating
    )

    db.add(new_stats)
    db.commit()
    db.refresh(new_stats)

    return new_stats

@router.delete("/{stats_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_stats(
    stats_id: int,
    db: Session = Depends(get_db)
):
    stats = get_stats_or_404(stats_id, db)

    db.delete(stats)
    db.commit()

