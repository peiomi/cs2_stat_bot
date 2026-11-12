from sqlalchemy import Column, Integer, String
from ..database.connection import Base

class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True)
    steam_id = Column(String, unique=True)
    player_name = Column(String nullable=False)
    discord_user_id = Column(Integer, ForeignKey("discord_members.id"))