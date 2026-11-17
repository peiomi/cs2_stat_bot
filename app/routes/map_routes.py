from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..database.util import get_db
from ..models.map import Map
from ..schemas.map_schema import MapCreate, MapResponse

router = APIRouter(prefix="/maps", tags=["Map"])

def get_map_or_404(
    map_id: int,
    db: Session
):
    cs_map = (
        db.query(Map)
        .filter(Map.id == map_id)
        .first()
    )
    if not cs_map:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Map not found"
        )

    return cs_map

@router.get("/", response_model=list[MapResponse])
def get_maps(db: Session = Depends(get_db)):
    return db.query(Map).all()

@router.get("/{map_id}", response_model=MapResponse)
def get_map(
    map_id: int,
    db: Session = Depends(get_db)
):
    return get_map_or_404(map_id, db)

@router.post("/", response_model=MapResponse, status_code=status.HTTP_201_CREATED)
def create_map(
    cs_map: MapCreate,
    db: Session = Depends(get_db)
):
    existing_map = (
        db.query(Map)
        .filter(Map.name == cs_map.name)
        .first()
    )

    if existing_map:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Map already exists"
        )

    new_map = Map(
        name=cs_map.name
    )

    db.add(new_map)
    db.commit()
    db.refresh(new_map)

    return new_map

@router.delete("/{map_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_map(
    map_id: int,
    db: Session = Depends(get_db)
):
    cs_map = get_map_or_404(map_id, db)

    db.delete(cs_map)
    db.commit()