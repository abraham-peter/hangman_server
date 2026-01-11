# Hangman Game - Server & Frontend

## Project Structure

```
hangman_server/
│
├── backend/                              # Backend FastAPI application
│   ├── src/                              # Source code
│   │   ├── main.py                       # Entry point FastAPI
│   │   ├── app.py                        # App configuration
│   │   ├── config.py                     # Configurări (DB, JWT, rate limits)
│   │   ├── database.py                   # DB connection, session maker
│   │   ├── models.py                     # Database models (SQLAlchemy)
│   │   │
│   │   ├── app/                          # Application module
│   │   │   ├── __init__.py
│   │   │   └── app.py                    # FastAPI app initialization
│   │   │
│   │   ├── routes/                       # API endpoints
│   │   │   ├── __init__.py
│   │   │   ├── auth.py                   # /auth/register, /auth/login
│   │   │   ├── sessions.py               # /sessions
│   │   │   ├── games.py                  # /games 
│   │   │   ├── words.py                  # /admin/dictionaries 
│   │   │   ├── stats.py                  # /stats, /leaderboard
│   │   │   └── health.py                 # /healthz, /version
│   │   │
│   │   ├── schemas/                      # Pydantic schemas (request/response)
│   │   │   ├── __init__.py
│   │   │   ├── auth.py                   # Login/Register schemas
│   │   │   ├── session.py                # Session request/response
│   │   │   ├── game.py                   # Game state schemas
│   │   │   ├── guess.py                  # Guess schemas
│   │   │   ├── stats.py                  # Statistics schemas
│   │   │   └── user.py                   # User schemas
│   │   │
│   │   ├── services/                     # Business logic
│   │   │   ├── __init__.py
│   │   │   ├── auth_service.py           # JWT, password hashing
│   │   │   ├── session_service.py        # Session management
│   │   │   ├── game_service.py           # Hangman logic 
│   │   │   ├── word_service.py           # Dictionary management 
│   │   │   └── stats_service.py          # Leaderboard, statistics
│   │   │
│   │   ├── middleware/                   # Custom middleware
│   │   │   ├── __init__.py
│   │   │   ├── auth.py                   # JWT validation
│   │   │   └── rate_limit.py             # Rate limiting
│   │   │
│   │   └── utils/                        # Helper functions
│   │       ├── __init__.py
│   │       ├── security.py               # Password hashing, token generation
│   │       ├── scoring.py                # Score calculation formula
│   │       └── validators.py             # Input validation helpers
│   │
│   └── tests/                            # Unit & integration tests
│       ├── __init__.py
│       ├── test_auth.py
│       ├── test_games.py
│       └── test_sessions.py
│
├── frontend/                             # Frontend web application
│   ├── html/                             # HTML templates
│   │   ├── difficulty.html
│   │   ├── game_menu.html
│   │   ├── login.html
│   │   ├── online_game.html
│   │   ├── options.html
│   │   ├── register.html
│   │   └── single_game.html
│   │
│   ├── css/                              # Stylesheets
│   │   ├── difficulty.css
│   │   ├── game_menu.css
│   │   ├── login.css
│   │   ├── online_game.css
│   │   ├── options.css
│   │   ├── register.css
│   │   └── single_game.css
│   │
│   ├── javascript/                       # Frontend logic
│   │   └── main.js
│   │
│   └── images/                           # Assets and images
│
├── docs/                                 # Documentation 
│   └── README.md                         # This file
│
├── hangman.py                            # Local hangman game
├── cuvant_din_db_criptat.py              # Word encryption utility
├── cuvinte.txt                           # Word dictionary
├── pyproject.toml                        # Python project configuration
├── uv.lock                               # Dependency lock file
├── .gitignore                            # Git ignore rules
├── .git/                                 # Git repository
└── .github/                              # GitHub configuration
```

## Architecture Overview

### Backend (FastAPI)
- **API Server**: FastAPI-based REST API with async support
- **Database**: SQLAlchemy ORM for data persistence
- **Authentication**: JWT-based authentication system
- **Services**: Business logic layer (auth, games, sessions, stats)
- **Schemas**: Pydantic models for request/response validation
- **Routes**: RESTful endpoints for all game functionality

### Frontend (HTML/CSS/JavaScript)
- **UI Pages**: Multiple game pages (login, register, game menu, etc.)
- **Styling**: Separate CSS for each page/feature
- **Client Logic**: JavaScript for interactivity and API communication

### Utilities
- `hangman.py`: Standalone hangman game implementation
- `cuvant_din_db_criptat.py`: Word encryption/decryption utilities
- `cuvinte.txt`: Dictionary of available words

## Key Features
- User authentication (register/login)
- Game session management
- Real-time game state tracking
- Leaderboard and statistics
- Rate limiting
- JWT-based security

## Getting Started
1. Install dependencies: `pip install -r backend/requirements.txt`
2. Configure environment variables
3. Run backend: `python backend/src/main.py`
4. Open frontend: Open HTML files in a browser
