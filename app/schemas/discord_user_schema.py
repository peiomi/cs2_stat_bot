from pydantic import BaseModel, ConfigDict

class DiscordUserBase(BaseModel):
    username: str
    discord_user_id: str

class DiscordUserCreate(DiscordUserBase):
    player_id: int

class DiscordUserResponse(DiscordUserBase):
    id: int
    player_id: int

    model_config = ConfigDict(from_attributes=True)

class DiscordUserUpdate(BaseModel):
    username: str | None = None