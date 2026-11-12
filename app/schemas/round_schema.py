from pydantic import BaseModel, ConfigDict

class RoundBase(BaseModel):
    round_number: int
    winning_side: str

class RoundCreate(RoundBase):
    match_id: int

class RoundResponse(RoundBase):
    id: int
    match_id: int

    model_config = ConfigDict(from_attributes=True)