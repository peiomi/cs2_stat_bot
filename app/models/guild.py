from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ..database.connection import Base

class Guild(Base):
    __tablename__ = "guilds"

    id = Column(Integer, primary_key=True)
    guild_id = Column(String, unique=True, nullable=False)
    name = Column(String, nullable=False)

    guild_members = relationship(
        "GuildMember",
        back_populates="guild"
    )