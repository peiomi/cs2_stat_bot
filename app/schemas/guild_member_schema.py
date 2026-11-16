from pydantic import BaseModel, ConfigDict

class GuildMemberBase(BaseModel):
    nickname: str | None = None
    member_role: str | None = None

class GuildMemberCreate(GuildMemberBase):
    discord_user_id: int

class GuildMemberResponse(GuildMemberBase):
    id: int
    guild_id: int
    discord_user_id: int

    model_config = ConfigDict(from_attributes=True)

class GuildMemberUpdate(BaseModel):
    nickname: str | None = None
    member_role: str | None = None