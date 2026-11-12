from pydantic import BaseModel, ConfigDict

class DiscordMemberBase(BaseModel):
    username: str
    discord_user_id: str
    member_role: str | None = None

class DiscordMemberCreate(DiscordMemberBase):
    server_id: int

class DiscordMemberResponse(DiscordMemberBase):
    id: int
    server_id: int

    model_config = ConfigDict(from_attributes=True)