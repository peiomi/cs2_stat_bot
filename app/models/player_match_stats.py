from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from ..database import Base

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

    cs_match = relationship(
        "Match",
        back_populates="player_stats"
    )

    player = relationship(
        "Player",
        back_populates="match_stats"
    )

    __table_args__ = (
        UniqueConstraint(
            "player_id",
            "match_id",
            name="uq_player_match"
        ),
    )