from pydantic import BaseModel, ConfigDict

class DiscordServerBase(BaseModel):
    guild_id: str
    name: str

class DiscordServerCreate(DiscordServerBase):
    pass

class DiscordServerResponse(DiscordServerBase):
    id: int

    model_config = ConfigDict(from_attributes=True)