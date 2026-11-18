from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ..database import Base

class Map(Base):
    __tablename__ = "maps"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)

    matches = relationship(
        "Match",
        back_populates="cs_map"
    )