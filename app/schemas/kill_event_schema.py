from pydantic import BaseModel, ConfigDict

class KillEventBase(BaseModel):
    weapon: str
    is_headshot: bool
    x: float 
    y: float 
    z: float = 0.0

class KillEventsCreate(KillEventBase):
    round_id: int
    match_id: int
    killer_id: int | None = None
    victim_id: int

class KillEventsResponse(KillEventBase):
    id: int
    match_id: int
    round_id: int
    killer_id: int | None
    victim_id: int

    model_config = ConfigDict(from_attributes=True)