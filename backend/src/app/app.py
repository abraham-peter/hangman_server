from fastapi import Depends, FastAPI
from fastapi_limiter import FastAPILimiter
from schemas.user import User,RegisterUser
from routes.games import router as games_router
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
    games_router,
    prefix="/game",
    tags=["game"]
)

    


# @app.get("/authenticated-route")
# async def authenticated_route(user: User = Depends(current_active_user)):
#     return {"message": f"Hello {user.email}!"}


# @app.on_event("startup")
# async def on_startup():
#     # Not needed if you setup a migration system like Alembic
#     await create_db_and_tables()
