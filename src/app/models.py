from sqlalchemy import Column, Integer, String, BigInteger
from .database import Base

class Country(Base):
    __tablename__ = "countries"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    capital = Column(String)
    population = Column(BigInteger)
    typical_dish = Column(String)