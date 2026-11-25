from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import Guild
from ..models import GuildMember
from ..schemas.guild_schema import GuildCreate, GuildResponse, GuildUpdate
from ..schemas.guild_member_schema import GuildMemberCreate, GuildMemberResponse, GuildMemberUpdate

router = APIRouter(prefix="/guilds", tags=["Guild"])

def get_guild_or_404(
    guild_id: int,
    db: Session
):
    guild = (
        db.query(Guild)
        .filter(Guild.id == guild_id)
        .first()
    )

    if not guild:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Guild not found"
        )

    return guild

def get_guild_member_or_404(
    guild_id: int,
    member_id: int,
    db: Session
):
    guild_member = (
        db.query(GuildMember)
        .filter(
            GuildMember.guild_id == guild_id,
            GuildMember.id == member_id
        )
        .first()
    )

    if not guild_member:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Guild member not found"
        )

    return guild_member

@router.get("/", response_model=list[GuildResponse])
def get_guilds(db: Session = Depends(get_db)):
    return db.query(Guild).all()

@router.get("/{guild_id}", response_model=GuildResponse)
def get_guild(
    guild_id: int,
    db: Session = Depends(get_db)
):
    return get_guild_or_404(guild_id, db)

@router.get("/guild-id/{guild_id}", response_model=GuildResponse)
def get_guild_by_guild_id(
    guild_id: int,
    db: Session = Depends(get_db)
):
    guild = (
        db.query(Guild)
        .filter(Guild.guild_id == guild_id)
        .first()
    )

    if not guild:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Guild not found"
        )

    return guild

@router.post("/", response_model=GuildResponse, status_code=status.HTTP_201_CREATED)
def create_guild(
    guild: GuildCreate,
    db: Session = Depends(get_db)
):
    existing_guild = (
        db.query(Guild)
        .filter(Guild.guild_id == guild.guild_id)
        .first()
    )

    if existing_guild:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Guild already exists"
        )

    new_guild = Guild(
        guild_id=guild.guild_id,
        name=guild.name
    )

    db.add(new_guild)
    db.commit()
    db.refresh(new_guild)

    return new_guild

@router.delete("/{guild_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_guild(
    guild_id: int,
    db: Session = Depends(get_db)
):
    guild = get_guild_or_404(guild_id, db)

    db.delete(guild)
    db.commit()

@router.put("/{guild_id}", response_model=GuildResponse)
def update_guild(
    guild_id: int,
    guild_update: GuildUpdate,
    db: Session = Depends(get_db)
):

    guild = get_guild_or_404(guild_id, db)

    if guild_update.name is not None:
        guild.name = guild_update.name

    db.commit()
    db.refresh(guild)

    return guild

@router.get("/{guild_id}/members", response_model=list[GuildMemberResponse])
def get_members(
    guild_id: int,
    db: Session = Depends(get_db)
):
    guild = get_guild_or_404(guild_id, db)

    return guild.guild_members

@router.get("/{guild_id}/members/{member_id}", response_model=GuildMemberResponse)
def get_member(
    guild_id: int,
    member_id: int,
    db: Session = Depends(get_db)
):

    member = get_guild_member_or_404(guild_id, member_id, db)

    return member

@router.post("/{guild_id}/members", response_model=GuildMemberResponse, status_code=status.HTTP_201_CREATED)
def create_guild_member(
    guild_id: int,
    member: GuildMemberCreate,
    db: Session = Depends(get_db)
):

    guild = get_guild_or_404(guild_id, db)

    existing_member = (
        db.query(GuildMember)
        .filter(
            GuildMember.guild_id == guild_id,
            GuildMember.discord_user_id == member.discord_user_id
        )
        .first()
    )

    if existing_member:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Member already exists in this guild"
        )

    new_member = GuildMember(
        nickname=member.nickname,
        guild_id=guild.id,
        discord_user_id=member.discord_user_id,
        member_role=member.member_role
    )

    db.add(new_member)
    db.commit()
    db.refresh(new_member)

    return new_member

@router.delete("/{guild_id}/members/{member_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_member(
    guild_id: int,
    member_id: int,
    db: Session = Depends(get_db)
):

    member = get_guild_member_or_404(guild_id, member_id, db)

    db.delete(member)
    db.commit()

@router.put("/{guild_id}/members/{member_id}", response_model=GuildMemberResponse)
def update_guild_member(
    guild_id: int,
    member_id: int,
    guild_member_update: GuildMemberUpdate,
    db: Session = Depends(get_db)
):

    member = get_guild_member_or_404(guild_id, member_id, db)

    if guild_member_update.nickname is not None:
        member.nickname = guild_member_update.nickname

    if guild_member_update.member_role is not None:
        member.member_role = guild_member_update.member_role

    db.commit()
    db.refresh(member)

    return member