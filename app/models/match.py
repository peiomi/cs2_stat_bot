from sqlalchemy import Column, Date, Integer, String, ForeignKey
from ..database.connection import Base

class Match(Base):
    __tablename__ = "matches"

    id = Column(Integer, primary_key=True)
    map_id = Column(Integer, ForeignKey("maps.id"), nullable=False)
    match_date = Column(Date, nullable=False)
    demo_filename = Column(String, unique=True, nullable=False)
    winning_team = Column(String)

    cs_map = relationship(
        "Map",
        back_populates="matches"
    )

    rounds = relationship(
        "Round",
        back_populates="match"
    )

    player_stats = relationship(
        "PlayerMatchStats",
        back_populates="match"
    )