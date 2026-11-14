from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Float
from ..database.connection import Base

class KillEvent(Base):
    __tablename__ = "kill_events"

    id = Column(Integer, primary_key=True)
    round_id = Column(Integer, ForeignKey("rounds.id"), nullable=False)
    match_id = Column(Integer, ForeignKey("matches.id"), nullable=False)
    killer_id = Column(Integer, ForeignKey("players.id"))
    victim_id = Column(Integer, ForeignKey("players.id"), nullable=False)
    weapon = Column(String, nullable=False)
    is_headshot = Column(Boolean, default=False, nullable=False)

    # players position during event
    x = Column(Float, nullable=False)
    y = Column(Float, nullable=False)
    z = Column(Float, nullable=False, default=0.0)

    match_round = relationship(
        "Round",
        back_populates="kill_events"
    )