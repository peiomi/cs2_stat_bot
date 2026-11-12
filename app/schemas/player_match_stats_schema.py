from pydantic import BaseModel, ConfigDict

class PlayerMatchStatsBase(BaseModel):
    kills: int
    deaths: int
    assists: int
    hs_kills: int
    adr: int
    rating: str | None = None

class PlayerMatchStatsCreate(PlayerMatchStatsBase):
    player_id: int
    match_id: int

class PlayerMatchStatsResponse(PlayerMatchStatsBase):
    id: int
    player_id: int
    match_id: int

    model_config = ConfigDict(from_attributes=True)
