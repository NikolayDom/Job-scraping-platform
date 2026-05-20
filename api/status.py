from fastapi import APIRouter
from db.company import Company
from db.engine import engine
from db.vacancy import Vacancy
from sqlalchemy.orm import Session

router = APIRouter()

@router.get("/status")
def get_status():
    session = Session(engine)
    vacancies_count = session.query(Vacancy).count()
    companies_count = session.query(Company).count()
    session.close()
    return {
        "status": "OK",
        "vacancies": vacancies_count,
        "companies": companies_count
    }