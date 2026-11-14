from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from ..database.connection import Base

class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True)
    steam_id = Column(String, unique=True, nullable=False)
    player_name = Column(String, nullable=False)
    discord_member_id = Column(Integer, ForeignKey("discord_members.id"))

    discord_member = relationship(
        "DiscordMember",
        back_populates="player"
    )

    match_stats = relationship(
        "PlayerMatchStats",
        back_populates="player"
    )

