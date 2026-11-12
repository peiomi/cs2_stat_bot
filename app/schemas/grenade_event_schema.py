from pydantic import BaseModel, ConfigDict

class GrenadeEventBase(BaseModel):
    grenade_type: GrenadeType
    damage: int = 0
    blind_time: float | None = None
    x: float 
    y: float 
    z: float = 0.0

class GrenadeEventCreate(GrenadeEventBase):
    round_id: int
    match_id: int
    player_id: int

class GrenadeEventResponse(GrenadeEventBase):
    id: int
    round_id: int
    match_id: int
    player_id: int

    model_config = ConfigDict(from_attributes=True)