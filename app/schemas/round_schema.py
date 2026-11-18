from pydantic import BaseModel, ConfigDict
from ..util.side_enum import Side

class RoundBase(BaseModel):
    round_number: int
    winning_side: Side

class RoundCreate(RoundBase):
    pass

class RoundResponse(RoundBase):
    id: int
    match_id: int

    model_config = ConfigDict(from_attributes=True)