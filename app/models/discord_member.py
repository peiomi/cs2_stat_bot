from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from ..database.connection import Base

class DiscordMember(Base):
    __tablename__ = "discord_members"

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    server_id = Column(Integer, ForeignKey("discord_servers.id"), nullable=False)
    discord_user_id = Column(String, unique=True, nullable=False)
    member_role = Column(String)

    server = relationship(
        "DiscordServer",
        back_populates="members"
    )

    player = relationship(
        "Player",
        back_populates="discord_member",
        uselist=False
    )