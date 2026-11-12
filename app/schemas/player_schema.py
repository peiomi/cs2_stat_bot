from pydantic import BaseModel

class PlayerBase(BaseModel):
    steam_id: str
    player_name: str

class PlayerCreate(PlayerBase):
    discord_user_id: int | None = None

class PlayerResponse(PlayerBase):
    id: int
    discord_user_id: int | None

    model_config = ConfigDict(from_attributes=True)