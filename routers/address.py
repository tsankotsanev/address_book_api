from db import crud
from db.database import get_db
from fastapi import APIRouter, Depends, Path, Query, status
from schemas import AddressBase, AddressDisplay
from sqlalchemy.orm.session import Session

router = APIRouter(
    prefix="/address",
    tags=["address"],
)


@router.post(
    "/create",
    response_model=AddressDisplay,
    status_code=status.HTTP_201_CREATED,
)
def create_address(request: AddressBase, db: Session = Depends(get_db)):
    return crud.create(db=db, request=request)


@router.get("/read/{id}", response_model=AddressDisplay)
def read_address(id: int = Path(..., gt=0), db: Session = Depends(get_db)):
    return crud.read(db, id)


@router.put("/update/{id}")
def update_address(
    request: AddressBase,
    id: int = Path(..., gt=0),
    db: Session = Depends(get_db),
):
    return crud.update(db, id, request)


@router.delete("/delete/{id}")
def delete_address(id: int = Path(..., gt=0), db: Session = Depends(get_db)):
    return crud.delete(db, id)


@router.get("/nearby/{id}")
def get_nearby_addresses(
    id: int = Path(..., gt=0),
    distance: float = Query(..., gt=0, description="Distance in kilometers"),
    db: Session = Depends(get_db),
):
    return crud.get_nearby_addresses(db, id, distance)
