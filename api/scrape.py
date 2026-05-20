from fastapi import APIRouter, BackgroundTasks
from scrapers.playwright_scraper import scrape_hh

router = APIRouter()

@router.post("/scrape")
def start_scrape(background_tasks: BackgroundTasks):
    background_tasks.add_task(scrape_hh)
    return {"status": "Сбор запущен"}