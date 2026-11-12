from pydantic import BaseModel, ConfigDict
from datetime import date

class MatchBase(BaseModel):
    match_date: date
    winning_team: str | None = None
    demo_filename: str

class MatchCreate(MatchBase):
    map_id: int

class MatchResponse(MatchBase):
    id: int
    map_id: int

    model_config = ConfigDict(from_attributes=True)