from sqlalchemy import Column, Integer, String
from ..database.connection import Base

class Map(Base):
    __tablename__ = "maps"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)