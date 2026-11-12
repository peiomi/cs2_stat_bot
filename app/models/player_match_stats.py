from sqlalchemy import Column, Integer, String, ForeignKey
from ..database.connection import Base

class PlayerMatchStats(Base):
    __tablename__ = "player_match_stats"

    id = Column(Integer, primary_key=True)
    player_id = Column(Integer, ForeignKey("players.id"), nullable=False)
    match_id = Column(Integer, ForeignKey("matches.id"), nullable=False)
    kills = Column(Integer, nullable=False)
    deaths = Column(Integer, nullable=False)
    assists = Column(Integer, nullable=False)
    hs_kills = Column(Integer, nullable=False)
    adr = Column(Integer, nullable=False)
    rating = Column(String)