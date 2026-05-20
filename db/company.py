from sqlalchemy import Column, Integer, String, DateTime
from db.base import Base

class Company(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key = True)
    name = Column(String)
    website = Column(String)
    created_at = Column(DateTime)