from fastapi import Depends, FastAPI
from fastapi_limiter import FastAPILimiter
from routes.sessions import router as sessions_router
from routes.games import router as games_router
from routes.health import router as health_router

import redis.asyncio as redis

app = FastAPI()

redis_client:redis.Redis | None=None
@app.on_event("startup")
async def startup():
    global redis_client

    redis_client=redis.from_url(
        "redis://localhost:6379",
        encoding="utf-8",
        decode_responses=True,
    )
    await FastAPILimiter.init(
        redis_client,
        key_prefix="hangman",
    )
@app.on_event("shutdown")
async def shutdown():
    if redis_client:
        await redis_client.close()


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

