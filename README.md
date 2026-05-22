# Job Scraping Platform

Асинхронная платформа для сбора и отображения данных о вакансиях.

## Что делает

Собирает данные о вакансиях с сайта hh.ru через Playwright, сохраняет их в PostgreSQL и предоставляет доступ через REST API на FastAPI.

## Стек

- Python 3.14
- Playwright
- FastAPI
- PostgreSQL
- SQLAlchemy
- Docker, Docker Compose
- GitHub Actions
- Alembic

## Архитектура

## Архитектура

## Архитектура

Playwright Scraper → PostgreSQL ← FastAPI REST API → User (Browser)

## Структура проекта

api/ (эндпоинты) → db/ (модели) → scrapers/ (Playwright) → alembic/ (миграции) → logs/ (логи) → app.py → config.py → logger.py → Dockerfile → docker-compose.yml → .github/ (CI/CD)

## Установка и запуск

Требуется Docker Desktop.

docker compose up --build

## Эндпоинты

| Метод | URL | Описание |
|---|---|---|
| GET | /vacancies | Список всех вакансий |
| GET | /vacancy/{id} | Одна вакансия по ID |
| POST | /scrape | Запустить сбор данных |
| GET | /status | Статус базы данных |

## Пример ответа

GET /vacancy/1
{
  "id": 1,
  "title": "Python-разработчик",
  "salary": "Не указана",
  "url": "https://hh.ru/vacancy/133211951?query=python&hhtmFrom=vacancy_search_list",
  "company": "ООО Компания Дилявер",
  "published_at": "2026-05-20 16:38:30.001293"
}