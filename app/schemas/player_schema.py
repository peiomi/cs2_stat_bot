from pydantic import BaseModel, field_validator, ConfigDict

class PlayerBase(BaseModel):
    steam_id: str
    player_name: str

    @field_validator("steam_id")
    @classmethod
    def validate_steam_id(cls, value):
        if not value.isdigit():
            raise ValueError("Steam ID must contain only digits")

        if len(value) != 17:
            raise ValueError("Steam ID must be 17 digits")

        return value

class PlayerCreate(PlayerBase):
    discord_member_id: int | None = None

class PlayerResponse(PlayerBase):
    id: int
    discord_member_id: int | None

    model_config = ConfigDict(from_attributes=True)

class PlayerUpdate(BaseModel):
    player_name: str | None = None
    discord_member_id: int | None = None