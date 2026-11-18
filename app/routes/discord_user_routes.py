from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import DiscordUser
from ..schemas.discord_user_schema import DiscordUserCreate, DiscordUserResponse, DiscordUserUpdate

from .player_routes import get_player_or_404

router = APIRouter(prefix="/discord-users", tags=["DiscordUsers"])

def get_discord_user_or_404(
    user_id: int,
    db: Session
):

    discord_user = (
        db.query(DiscordUser)
        .filter(DiscordUser.id == user_id)
        .first()
    )

    if not discord_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    return discord_user

@router.get("/", response_model=list[DiscordUserResponse])
def get_discord_users(db: Session = Depends(get_db)):
    return db.query(DiscordUser).all()

@router.get("/{user_id}", response_model=DiscordUserResponse)
def get_discord_user(
    user_id: int,
    db: Session = Depends(get_db)
):
    return get_discord_user_or_404(user_id, db)

@router.post("/", response_model=DiscordUserResponse, status_code=status.HTTP_201_CREATED)
def create_discord_user(
    user: DiscordUserCreate,
    db: Session = Depends(get_db)
):
    get_player_or_404(user.player_id, db)

    existing_user = (
        db.query(DiscordUser)
        .filter(DiscordUser.discord_user_id == user.discord_user_id)
        .first()
    )

    existing_player = (
        db.query(DiscordUser)
        .filter(DiscordUser.player_id == user.player_id)
        .first()
    )

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User with this discord user ID already exists"
        )

    if existing_player:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Player already linked to a Discord user"
        )

    new_discord_user = DiscordUser(
        username=user.username,
        discord_user_id=user.discord_user_id,
        player_id=user.player_id
    )

    db.add(new_discord_user)
    db.commit()
    db.refresh(new_discord_user)

    return new_discord_user

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_discord_user(
    user_id: int,
    db: Session = Depends(get_db)
):

    discord_user = get_discord_user_or_404(user_id, db)
    db.delete(discord_user)
    db.commit()

@router.patch("/{user_id}", response_model=DiscordUserResponse)
def update_discord_user(
    user_id: int,
    user_update: DiscordUserUpdate,
    db: Session = Depends(get_db)
):

    discord_user = get_discord_user_or_404(user_id, db)

    if user_update.username is not None:
        discord_user.username = user_update.username

    db.commit()
    db.refresh(discord_user)

    return discord_user