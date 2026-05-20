from sqlalchemy import Column, Integer, String, DateTime
from db.base import Base

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    name = Column(String)