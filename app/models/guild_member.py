from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from ..database.connection import Base

class GuildMember(Base):
    __tablename__ = "guild_members"

    id = Column(Integer, primary_key=True)
    nickname = Column(String)
    guild_id = Column(Integer, ForeignKey("guilds.id"), nullable=False)
    discord_user_id = Column(Integer, ForeignKey("discord_users.id"), nullable=False)
    member_role = Column(String)

    discord_user = relationship(
        "DiscordUser",
        back_populates="guild_memberships"
    )

    guild = relationship(
        "Guild",
        back_populates="guild_members"
    )

    __table_args__ = (
        UniqueConstraint(
            "guild_id",
            "discord_user_id",
            name="uq_guild_user"
        ),
    )