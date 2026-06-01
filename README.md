# 🚀 DevSecOps-pipeline-demo
<img width="1700" height="955" alt="image" src="https://github.com/user-attachments/assets/d2ca6470-e439-4fc1-b53f-b6cb424afe57" />


A FastAPI-based REST API built during a hackathon. Fully containerized with Docker, automatically tested and deployed to Railway via GitHub Actions CI/CD pipeline with security scanning powered by Trivy.

🌍 **Live:** [devsecops-pipeline-demo-production.up.railway.app](https://devsecops-pipeline-demo-production.up.railway.app/)

## ✨ Features

- REST API built with FastAPI
- Beautiful landing page at `/`
- Automatic API docs at `/docs` (Swagger UI) and `/redoc`
- Dockerized — runs the same everywhere
- CI/CD pipeline: lint → test → security scan → deploy
- Telegram notifications on every build

## 📋 Requirements

- [Docker](https://docs.docker.com/get-docker/) + Docker Compose
- Python 3.12+ (for local development without Docker)

## ⚡ Quick Start

```bash
# 1. Clone the repo
git clone <repo-url> && cd crispy-giggle

# 2. Create environment file
cp .env.example .env

# 3. Run with Docker (recommended)
docker compose up --build

# Or run locally without Docker
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Local app: **http://localhost:8000**  
Production: **devsecops-pipeline-demo-production.up.railway.app**  
API documentation: **https://devsecops-pipeline-demo-production.up.railway.app/docs**

## 🗂️ Project Structure

```
crispy-giggle/
├── app/
│   ├── __init__.py
│   └── main.py           # FastAPI entry point + landing page
├── tests/
│   └── test_main.py      # Pytest test suite (16 tests)
├── .github/
│   └── workflows/
│       ├── ci.yml        # Lint + Test + Trivy security scan
│       └── cd.yml        # Auto-deploy to Railway
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── pytest.ini
├── .env.example
└── .gitignore
```

## 🔄 CI/CD Pipeline

Every push to `main` triggers the full pipeline:

```
push to main
    │
    ├── CI
    │   ├── Lint          (ruff)
    │   ├── Tests         (pytest)
    │   ├── Security scan (Trivy — CRITICAL/HIGH)
    │   └── Notify        (Telegram)
    │
    └── CD  (only if CI passes)
        ├── Deploy to Railway
        └── Notify (Telegram)
```

## 🔐 GitHub Secrets

Configure these in **Settings → Secrets → Actions** before running the pipeline:

| Secret | Description |
|--------|-------------|
| `RAILWAY_TOKEN` | Railway API token (Account Settings → Tokens) |
| `RAILWAY_SERVICE_NAME` | Service name in your Railway project |
| `RAILWAY_PUBLIC_URL` | Public URL after deployment |
| `TELEGRAM_TO` | Telegram chat ID for notifications |
| `TELEGRAM_TOKEN` | Telegram bot token |

## 🌍 Environment Variables

Copy `.env.example` to `.env` and fill in the values:

```env
APP_ENV=development
APP_PORT=8000
```

> ⚠️ Never commit `.env` to Git — it is listed in `.gitignore`.

## 🧪 Running Tests

```bash
pytest tests/ -v
```

16 tests covering all endpoints: landing page, health check, full Items CRUD, and Messages.

## 🐳 Docker

```bash
# Build image
docker build -t crispy-giggle .

# Run container
docker run -p 8000:8000 crispy-giggle

# Run with compose
docker compose up --build
```

## 🛡️ Security

This project uses [Trivy](https://trivy.dev) to scan for vulnerabilities on every CI run. Any `CRITICAL` or `HIGH` severity finding will fail the pipeline and block deployment.

## 📬 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Landing page |
| GET | `/health` | Service status + timestamp |
| GET | `/docs` | Swagger UI |
| GET | `/redoc` | ReDoc documentation |
| GET | `/items` | List all items |
| POST | `/items` | Create a new item |
| GET | `/items/{id}` | Get item by ID |
| DELETE | `/items/{id}` | Delete item by ID |
| GET | `/messages` | List all messages |
| POST | `/messages` | Post a new message |

### Item schema

```json
{
  "name": "Widget",
  "description": "Optional description",
  "price": 9.99,
  "in_stock": true
}
```

### Message schema

```json
{
  "text": "Hello world",
  "author": "alice"
}
```
