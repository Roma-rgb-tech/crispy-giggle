# Hackathon Project

## Швидкий старт

```bash
# 1. Клонуй репо
git clone <repo-url> && cd <repo>

# 2. Створи .env
cp .env.example .env

# 3. Запусти локально
docker compose up --build
# або без Docker:
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Застосунок доступний на http://localhost:8000
Документація API: http://localhost:8000/docs

## Структура

```
app/
  main.py        # Точка входу FastAPI
tests/
  test_main.py   # Тести
.github/workflows/
  ci.yml         # Lint + Test + Trivy scan
  cd.yml         # Автодеплой на Railway
```

## GitHub Secrets (налаштовує DevSecOps)

| Secret | Опис |
|--------|------|
| `RAILWAY_TOKEN` | API токен Railway |
| `RAILWAY_SERVICE_NAME` | Назва сервісу в Railway |
| `RAILWAY_PUBLIC_URL` | Публічний URL після деплою |
| `TELEGRAM_TO` | Chat ID для нотифікацій |
| `TELEGRAM_TOKEN` | Telegram Bot Token |

## CI/CD Flow

```
push → CI (lint → test → trivy) → CD (railway deploy) → Telegram
```