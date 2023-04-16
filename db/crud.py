from db.models import DbAddress
from fastapi import status
from fastapi.exceptions import HTTPException
from schemas import AddressBase
from sqlalchemy.orm.session import Session
from haversine import haversine, Unit
from custom_log import log


not_found_exc = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Address not found",
)


def create(db: Session, request: AddressBase):
    new_address = DbAddress(
        street=request.street,
        city=request.city,
        country=request.country,
        latitude=request.latitude,
        longitude=request.longitude,
    )
    db.add(new_address)
    db.commit()
    db.refresh(new_address)
    if new_address:
        log("Call to create address", "Success")
    return new_address


def read(db: Session, id: int):
    address = db.query(DbAddress).filter(DbAddress.id == id).first()
    if not address:
        log("Call to read address", "Failure")
        raise not_found_exc
    log("Call to read address", "Success")
    return address


def update(db: Session, id: int, request: AddressBase):
    address = read(db, id)
    if not address:
        log("Call to update address", "Failure")
        raise not_found_exc
    address.street = request.street
    address.city = request.city
    address.country = request.country
    address.latitude = request.latitude
    address.longitude = request.longitude
    db.commit()
    log("Call to update address", "Success")
    return f"Address with id {id} updated successfully"


def delete(db: Session, id: int):
    address = read(db, id)
    if not address:
        log("Call to delete address", "Failure")
        raise not_found_exc
    db.delete(address)
    db.commit()
    log("Call to delete address", "Success")
    return f"Address with id {id} deleted successfully"


def get_nearby_addresses(db: Session, id: int, distance: float):
    address = read(db, id)
    if not address:
        raise not_found_exc
    addresses = db.query(DbAddress).filter(DbAddress.id != id).all()
    nearby_addresses = []
    for addr in addresses:
        if (
            haversine(
                (address.latitude, address.longitude),
                (addr.latitude, addr.longitude),
                unit=Unit.KILOMETERS,
            )
            < distance
        ):
            nearby_addresses.append(addr)
    if not nearby_addresses:
        log("Call to get nearby addresses", "Failure")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No addresses within {distance} "
            f"kilometers of address with id {id}",
        )
    log("Call to get nearby addresses", "Success")
    return nearby_addresses
