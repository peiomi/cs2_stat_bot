from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ..database.connection import Base

class DiscordServer(Base):
    __tablename__ = "discord_servers"

    id = Column(Integer, primary_key=True)
    guild_id = Column(String, unique=True, nullable=False)
    name = Column(String, nullable=False)

    members = relationship(
        "DiscordMember",
        back_populates="server"
    )