from fastapi import FastAPI
from api.vacancies import router as vacancies_router
from api.scrape import router as scrape_router
from api.status import router as status_router

app = FastAPI()

app.include_router(vacancies_router)

app.include_router(scrape_router)

app.include_router(status_router)