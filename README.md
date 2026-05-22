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

┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│  Playwright │────▶│  PostgreSQL  │◀────│   FastAPI    │
│  Scraper    │     │  (Docker)    │     │   REST API   │
└─────────────┘     └─────────────┘     └─────────────┘
                           │
                           ▼
                    ┌─────────────┐
                    │    User     │
                    │  (Browser)  │
                    └─────────────┘

## Структура проекта

job-scraping-platform/
├── api/            # эндпоинты FastAPI
├── db/             # модели SQLAlchemy
├── scrapers/       # скраперы (Playwright)
├── alembic/        # миграции базы данных
├── logs/           # логи
├── app.py          # точка входа FastAPI
├── config.py       # настройки
├── logger.py       # логирование
├── Dockerfile
├── docker-compose.yml
└── .github/        # CI/CD

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