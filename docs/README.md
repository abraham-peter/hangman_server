Deci lucram dupa aceasta structura:
hangman_server/
│
├── backend/
│   ├── server/
│   │   ├── src/
│   │   │   ├── app.py                    # Entry point FastAPI
│   │   │   ├── config.py                 # Configurări (DB, JWT, rate limits)
│   │   │   │
│   │   │   ├── models/                   # Database models (SQLAlchemy/Pydantic)
│   │   │   │   ├── __init__.py
│   │   │   │   ├── user.py               # [LIPSEȘTE] User model
│   │   │   │   ├── session.py            # [LIPSEȘTE] Session model
│   │   │   │   ├── game.py               # Game model ✓
│   │   │   │   ├── word.py               # Word/Dictionary model ✓
│   │   │   │   └── guess.py              # [LIPSEȘTE] Guess model
│   │   │   │
│   │   │   ├── schemas/                  # [LIPSEȘTE FOLDER] Pydantic schemas (request/response)
│   │   │   │   ├── __init__.py
│   │   │   │   ├── auth.py               # Login/Register schemas
│   │   │   │   ├── session.py            # Session request/response
│   │   │   │   ├── game.py               # Game state schemas
│   │   │   │   └── stats.py              # Statistics schemas
│   │   │   │
│   │   │   ├── routes/                   # API endpoints
│   │   │   │   ├── __init__.py
│   │   │   │   ├── auth.py               # [LIPSEȘTE] /auth/register, /auth/login
│   │   │   │   ├── sessions.py           # [LIPSEȘTE] /sessions
│   │   │   │   ├── games.py              # /games ✓
│   │   │   │   ├── words.py              # /admin/dictionaries ✓
│   │   │   │   ├── stats.py              # [LIPSEȘTE] /stats, /leaderboard
│   │   │   │   └── health.py             # [LIPSEȘTE] /healthz, /version
│   │   │   │
│   │   │   ├── services/                 # Business logic
│   │   │   │   ├── __init__.py
│   │   │   │   ├── auth_service.py       # [LIPSEȘTE] JWT, password hashing
│   │   │   │   ├── session_service.py    # [LIPSEȘTE] Session management
│   │   │   │   ├── game_service.py       # Hangman logic ✓
│   │   │   │   ├── word_service.py       # Dictionary management ✓
│   │   │   │   └── stats_service.py      # [LIPSEȘTE] Leaderboard, statistics
│   │   │   │
│   │   │   ├── middleware/               # [LIPSEȘTE FOLDER] Custom middleware
│   │   │   │   ├── __init__.py
│   │   │   │   ├── auth.py               # JWT validation
│   │   │   │   └── rate_limit.py         # Rate limiting
│   │   │   │
│   │   │   ├── utils/                    # [LIPSEȘTE FOLDER] Helper functions
│   │   │   │   ├── __init__.py
│   │   │   │   ├── security.py           # Password hashing, token generation
│   │   │   │   ├── scoring.py            # Score calculation formula
│   │   │   │   └── validators.py         # Input validation helpers
│   │   │   │
│   │   │   └── database.py               # [LIPSEȘTE] DB connection, session maker
│   │   │
│   │   ├── migrations/                   # Database migrations (Alembic)
│   │   │   └── [Va fi generat automat]
│   │   │
│   │   ├── tests/                        # Unit & integration tests
│   │   │   ├── __init__.py
│   │   │   ├── test_auth.py
│   │   │   ├── test_games.py
│   │   │   └── test_sessions.py
│   │   │
│   │   ├── openapi.yaml                  # API documentation ✓
│   │   ├── requirements.txt              # [LIPSEȘTE] Python dependencies
│   │   └── .env.example                  # [LIPSEȘTE] Environment variables example
│   │
│   └── client_examples/                  # Example clients ✓
│       ├── python_client.py
│       └── postman_collection.json
│
├── docker/                               # Docker setup ✓
│   ├── Dockerfile
│   └── docker-compose.yaml
│
├── docs/                                 # Documentation ✓
│   └── README.md
│
├── .gitignore                            # [LIPSEȘTE] Git ignore rules
<!-- └── README.md                             # [LIPSEȘTE] Project overview -->