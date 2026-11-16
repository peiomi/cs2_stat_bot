from pydantic import BaseModel, ConfigDict

class GuildBase(BaseModel):
    guild_id: str
    name: str

class GuildCreate(GuildBase):
    pass

class GuildResponse(GuildBase):
    id: int

    model_config = ConfigDict(from_attributes=True)

class GuildUpdate(BaseModel):
    name: str | None = None