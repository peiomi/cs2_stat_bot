from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from ..database import Base

class DiscordUser(Base):
    __tablename__ = "discord_users"

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    discord_user_id = Column(String, unique=True, nullable=False)
    player_id = Column(Integer, ForeignKey("players.id"), unique=True, nullable=False)

    guild_memberships = relationship(
        "GuildMember",
        back_populates="discord_user"
    )

    player = relationship(
        "Player",
        back_populates="discord_user"
    )