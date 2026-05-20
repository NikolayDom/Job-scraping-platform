from playwright.async_api import async_playwright
import asyncio
import re
from sqlalchemy.orm import Session
from db.base import Base
from db.category import Category
from db.vacancy import Vacancy
from db.company import Company
from db.engine import engine
from datetime import datetime

async def scrape_hh():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        url = "https://hh.ru/search/vacancy?text=python&area=1"
        await page.goto(url)
        await page.wait_for_selector('[data-qa="vacancy-serp__vacancy"]')
        cards = await page.query_selector_all('[data-qa="vacancy-serp__vacancy"]')  
        vacancies = []
        for card in cards:
            title_el = await card.query_selector('[data-qa="serp-item__title-text"]')
            title = await title_el.text_content()

            full_card_text = await card.text_content()
            salary_match = re.search(r'(?:от|до)\s[\d\s]*[₽руб]', full_card_text)
            salary = salary_match.group(0) if salary_match else "Не указана"
            salary = salary.replace('\xa0', ' ').replace('\u202f', ' ') if salary != "Не указана" else salary

            link_el = await card.query_selector('[data-qa="serp-item__title"]')
            link = await link_el.get_attribute("href") if link_el else ""

            company_el = await card.query_selector('[data-qa="vacancy-serp__vacancy-employer-text"]')
            company = await company_el.text_content()
            company = company.replace('\xa0', ' ').replace('\u202f', ' ')

            vacancy = {
                "title": title,
                "salary": salary,
                "link": link,
                "company": company
            }

            vacancies.append(vacancy)

        await browser.close()

        Base.metadata.create_all(engine)
        session = Session(engine)
        
        for vacancy in vacancies:
            company_name = vacancy["company"]
            company = session.query(Company).filter(Company.name == company_name).first()
            if company is None:
                company = Company(name=company_name)
                session.add(company)
                session.flush()
            
            new_vacancy = Vacancy(
                title = vacancy["title"],
                salary = vacancy["salary"],
                url = vacancy["link"],
                company_id = company.id,
                published_at = datetime.now()
            )
            session.add(new_vacancy)
        
        session.commit()
        session.close()
        
        return vacancies
 
if __name__ == "__main__":   
    result = asyncio.run(scrape_hh())
    print(result)