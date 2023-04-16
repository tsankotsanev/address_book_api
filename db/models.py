from sqlalchemy import Column
from sqlalchemy.types import Integer, String, Float

from db.database import Base


class DbAddress(Base):
    __tablename__ = "addresses"

    id = Column(Integer, primary_key=True, index=True)
    street = Column(String)
    city = Column(String)
    country = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
