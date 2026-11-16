from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from ..database.connection import Base

class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True)
    steam_id = Column(String, unique=True, nullable=False)
    player_name = Column(String, nullable=False)

    discord_user = relationship(
        "DiscordUser",
        back_populates="player",
        uselist=False
    )

    guild_member = relationship(
        "GuildMember",
        back_populates="player"
    )

    match_stats = relationship(
        "PlayerMatchStats",
        back_populates="player"
    )

