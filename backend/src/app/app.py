from fastapi import Depends, FastAPI
from schemas.user import User,RegisterUser
from middleware.auth import auth_backend, current_active_user, fastapi_users
from routes.games import router as games_router

app = FastAPI()

app.include_router(
    fastapi_users.get_auth_router(auth_backend), prefix="/auth/jwt", tags=["auth"]
)
app.include_router(
    fastapi_users.get_register_router(User, RegisterUser),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_reset_password_router(),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_verify_router(User),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_users_router(User, RegisterUser),
    prefix="/users",
    tags=["users"],
)
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
