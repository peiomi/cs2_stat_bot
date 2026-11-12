from sqlalchemy import Column, Integer, String, ForeignKey, Float, Enum
from ..database.connection import Base
from ..util.grenade_enum import GrenadeType

class GrenadeEvent(Base):
    __tablename__ = "grenade_events"

    id = Column(Integer, primary_key=True)
    round_id = Column(Integer, ForeignKey("rounds.id"), nullable=False)
    match_id = Column(Integer, ForeignKey("matches.id"), nullable=False)
    player_id = Column(Integer, ForeignKey("players.id"), nullable=False)
    grenade_type = Column(Enum(GrenadeType), nullable=False)
    damage = Column(Integer, nullable=False, default=0)
    blind_time = Column(Float)

    x = Column(Float, nullable=False)
    y = Column(Float, nullable=False)
    z = Column(Float, nullable=False, default=0.0)