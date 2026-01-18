from fastapi import Depends, FastAPI
from fastapi_limiter import FastAPILimiter
from fastapi.middleware.cors import CORSMiddleware
from routes.sessions import router as sessions_router
from routes.games import router as games_router
from routes.health import router as health_router
from routes.auth import router as auth_router
import redis.asyncio as redis

import os

app = FastAPI()

# Allow all origins by default for initial deployment (change in production)
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

redis_client: redis.Redis | None = None

@app.on_event("startup")
async def startup():
    global redis_client
    redis_url = os.getenv("REDIS_URL")
    if redis_url:
        redis_client = redis.from_url(
            redis_url,
            encoding="utf-8",
            decode_responses=True,
        )
        await FastAPILimiter.init(redis_client)

@app.on_event("shutdown")
async def shutdown():
    if redis_client:
        await redis_client.close()

app.include_router(
    auth_router,
    prefix="/auth",
    tags=["auth"],
)

app.include_router(
    sessions_router,
    prefix="/sessions",
    tags=["sessions"],
)

app.include_router(
    games_router,
    prefix="/game",
    tags=["game"],
)
app.include_router(
    health_router,
    prefix="/health",
    tags=["health"],
)

