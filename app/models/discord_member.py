from sqlalchemy import Column, Integer, String, ForeignKey
from ..database.connection import Base

class DiscordMember(Base):
    __tablename__ = "discord_members"

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    server_id = Column(Integer, ForeignKey("discord_servers.id"), nullable=False)
    discord_user_id = Column(String, nullable=False)
    member_role = Column(String)