from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..database.util import get_db
from ..models.player import Player
from ..schemas.player_schema import PlayerResponse, PlayerCreate, PlayerUpdate


router = APIRouter(prefix="/players", tags=["Players"])

def get_player_or_404(
    player_id: int,
    db: Session
):
    player = (
        db.query(Player)
        .filter(Player.id == player_id)
        .first()
    )
    if not player:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Player not found"
        )

    return player


@router.get("/", response_model=list[PlayerResponse])
def get_players(
    db: Session = Depends(get_db)
):
    return db.query(Player).all()


@router.get("/{player_id}", response_model=PlayerResponse)
def get_player(
    player_id: int,
    db: Session = Depends(get_db)
):

    return get_player_or_404(player_id, db)

@router.post("/", response_model=PlayerResponse, status_code=status.HTTP_201_CREATED)
def create_player(
    player: PlayerCreate, 
    db: Session = Depends(get_db)
):
    existing_player = (
        db.query(Player)
        .filter(Player.steam_id == player.steam_id)
        .first()
    )

    if existing_player:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Player with this Steam ID already exists"
        )

    new_player = Player(
        steam_id=player.steam_id,
        player_name=player.player_name,
        discord_member_id=player.discord_member_id
    )

    db.add(new_player)
    db.commit()
    db.refresh(new_player)

    return new_player

@router.delete("/{player_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_player(
    player_id: int,
    db: Session = Depends(get_db)
):

    player = get_player_or_404(player_id, db)

    db.delete(player)
    db.commit()

@router.put("/{player_id}", response_model=PlayerResponse)
def update_player(
    player_id: int,
    player_update: PlayerUpdate,
    db: Session = Depends(get_db)
):

    player = get_player_or_404(player_id, db)

    if player_update.player_name is not None:
        player.player_name = player_update.player_name

    if player_update.discord_member_id is not None:
        player.discord_member_id = player_update.discord_member_id

    db.commit()
    db.refresh(player)

    return player
