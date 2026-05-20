from db.base import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey

class Vacancy(Base):
    __tablename__ = "vacancies"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    salary = Column(String, nullable=True)
    url = Column(String, nullable=True)
    published_at = Column(DateTime)
    company_id = Column(Integer, ForeignKey("companies.id"))
    category_id = Column(Integer, ForeignKey("categories.id"))