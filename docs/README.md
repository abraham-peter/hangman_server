# 🎮 Hangman Game - Full Stack Application

## Status: Production Ready ✅

## Quick Start

```bash
# Install
pip install -r requirements.txt

# Run
cd backend/src && python main.py
```

Server: `http://localhost:8000`  
API Docs: `http://localhost:8000/docs`

## Project Structure

```
hangman_server/
├── backend/
│   ├── src/
│   │   ├── main.py              # Entry point
│   │   ├── config.py            # Configuration
│   │   ├── database.py          # DB setup
│   │   ├── models.py            # SQLAlchemy models
│   │   ├── app/
│   │   │   └── app.py           # FastAPI app
│   │   ├── routes/              # API endpoints
│   │   │   ├── auth.py          # /auth/*
│   │   │   ├── sessions.py      # /sessions/*
│   │   │   ├── games.py         # /game/*
│   │   │   ├── words.py         # /admin/dictionaries
│   │   │   ├── stats.py         # /stats/*
│   │   │   └── health.py        # /health/*
│   │   ├── schemas/             # Pydantic models
│   │   ├── services/            # Business logic
│   │   ├── middleware/          # Auth, rate limiting
│   │   └── utils/               # Helpers
│   └── tests/
├── frontend/
│   ├── html/                    # Pages
│   ├── css/                     # Styles
│   ├── js/                      # Frontend logic
│   └── assets/                  # Images
├── docs/
├── requirements.txt
├── Dockerfile
└── render.yaml
```


