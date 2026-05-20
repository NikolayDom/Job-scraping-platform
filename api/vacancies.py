from fastapi import APIRouter
from db.engine import engine
from sqlalchemy.orm import Session
from db.vacancy import Vacancy
from db.company import Company
from fastapi import HTTPException

router = APIRouter()

@router.get("/vacancies")
def get_vacancies():
    session = Session(engine)
    vacancies = session.query(Vacancy).all()
    
    result = []
    for v in vacancies:
        company = session.query(Company).filter(Company.id == v.company_id).first()
        result.append({
            "id": v.id,
            "title": v.title,
            "salary": v.salary,
            "url": v.url,
            "company_id": v.company_id,
            "published_at": str(v.published_at),
            "company": company.name if company else "Не указана"
        })

    session.close()

    return result

@router.get("/vacancy/{vacancy_id}")
def get_vacancy(vacancy_id: int):
    session = Session(engine)
    vacancy = session.query(Vacancy).filter(Vacancy.id == vacancy_id).first()

    if vacancy is None:
        raise HTTPException(status_code=404, detail="Вакансия не найдена")
    
    company = session.query(Company).filter(Company.id == vacancy.company_id).first()
    
    session.close()
    
    return {
        "id": vacancy.id,
        "title": vacancy.title,
        "salary": vacancy.salary,
        "url": vacancy.url,
        "company": company.name if company else "Не указана",
        "published_at": str(vacancy.published_at)
    }