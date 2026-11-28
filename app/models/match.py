from sqlalchemy import Column, Date, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from ..database import Base

class Match(Base):
    __tablename__ = "matches"

    id = Column(Integer, primary_key=True)
    file_hash = Column(String(64), unique=True, nullable=False)
    map_id = Column(Integer, ForeignKey("maps.id"), nullable=False)
    match_date = Column(Date, nullable=False)
    demo_filename = Column(String, nullable=False)
    winning_team = Column(String)

    cs_map = relationship(
        "Map",
        back_populates="matches"
    )

    rounds = relationship(
        "Round",
        back_populates="cs_match",
        cascade="all, delete-orphan"
    )

    player_stats = relationship(
        "PlayerMatchStats",
        back_populates="cs_match",
        cascade="all, delete-orphan"
    )