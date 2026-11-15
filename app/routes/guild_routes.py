from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..database.util import get_db
from ..models.discord_server import DiscordServer
from ..schemas.discord_server_schema import DiscordServerCreate, DiscordServerResponse, DiscordServerUpdate

router = APIRouter(prefix="/guilds", tags=["DiscordServer"])

def get_guild_or_404(
    server_id: int,
    db: Session
):
    guild = (
        db.query(DiscordServer)
        .filter(DiscordServer.id == server_id)
        .first()
    )

    if not guild:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Guild not found"
        )

    return guild

@router.get("/", response_model=list[DiscordServerResponse])
def get_guilds(db: Session = Depends(get_db)):
    return db.query(DiscordServer).all()

@router.get("/{server_id}", response_model=DiscordServerResponse)
def get_guild(
    server_id: int,
    db: Session = Depends(get_db)
):
    return get_guild_or_404(server_id, db)

@router.post("/", response_model=DiscordServerResponse, status_code=status.HTTP_201_CREATED)
def create_guild(
    guild: DiscordServerCreate,
    db: Session = Depends(get_db)
):
    existing_guild = (
        db.query(DiscordServer)
        .filter(DiscordServer.guild_id == guild.guild_id)
        .first()
    )

    if existing_guild:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Guild already exists"
        )

    new_guild = DiscordServer(
        guild_id=guild.guild_id,
        name=guild.name
    )

    db.add(new_guild)
    db.commit()
    db.refresh(new_guild)

    return new_guild

@router.delete("/{server_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_guild(
    server_id: int,
    db: Session = Depends(get_db)
):
    guild = get_guild_or_404(server_id, db)

    db.delete(guild)
    db.commit()

@router.put("/{server_id}", response_model=DiscordServerResponse)
def update_guild(
    server_id: int,
    server_update: DiscordServerUpdate,
    db: Session = Depends(get_db)
):

    guild = get_guild_or_404(server_id, db)

    if server_update.name is not None:
        guild.name = server_update.name

    db.commit()
    db.refresh(guild)

    return guild