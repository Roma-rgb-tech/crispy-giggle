# Hackathon Project

## Quick Start

# 1. Clone the repo
git clone <repo-url> && cd <repo>

# 2. Create .env
cp .env.example .env

# 3. Run locally
docker compose up --build
# or without Docker:
pip install -r requirements.txt
uvicorn app.main:app --reload
The application is available at http://localhost:8000
API Documentation: http://localhost:8000/docs

# Structure

app/
  main.py        # FastAPI entry point
tests/
  test_main.py   # Tests
.github/workflows/
  ci.yml         # Lint + Test + Trivy scan
  cd.yml         # Auto-deploy to Railway


# CI/CD Flow
push → CI (lint → test → trivy) → CD (railway deploy) → Telegram
