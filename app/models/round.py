from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from ..database import Base

class Round(Base):
    __tablename__ = "rounds"

    id = Column(Integer, primary_key=True)
    match_id = Column(Integer, ForeignKey("matches.id"), nullable=False)
    round_number = Column(Integer, nullable=False)
    winning_side = Column(String, nullable=False)

    cs_match = relationship(
        "Match",
        back_populates="rounds"
    )

    kill_events = relationship(
        "KillEvent",
        back_populates="match_round"
    )

    grenade_events = relationship(
        "GrenadeEvent",
        back_populates="match_round"
    )

    __table_args__ = (
        UniqueConstraint(
            "match_id",
            "round_number",
            name="uq_match_round"
        ),
    )