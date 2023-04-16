from pydantic import BaseModel, validator


class AddressBase(BaseModel):
    street: str
    city: str
    country: str
    latitude: float
    longitude: float

    @validator("street", "city", "country")
    def check_length(cls, value):
        if len(value) > 255:
            raise ValueError(
                "The input must be less than or equal to 255 characters."
            )
        return value

    @validator("city", "country")
    def check_alpha(cls, value):
        if not value.isalpha():
            raise ValueError("Must only contain letters!")
        return value

    @validator("latitude")
    def check_latitude(cls, value):
        if not -90 <= value <= 90:
            raise ValueError("Latitude must be between -90 and 90")
        return value

    @validator("longitude")
    def check_longitude(cls, value):
        if not -180 <= value <= 180:
            raise ValueError("Longitude must be between -180 and 180")
        return value


class AddressDisplay(BaseModel):
    street: str
    city: str
    country: str
    latitude: float
    longitude: float

    class Config:
        orm_mode = True
