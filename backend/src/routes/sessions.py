from fastapi import APIRouter,status,Depends
from typing import Annotated
from routes.auth import get_current_active_user
from schemas.user import User
router=APIRouter()


@router.get("/session/{session_id}/stats",status_code=status.HTTP_201_CREATED)
async def stats(session_id:str,
                current_user:Annotated[User,Depends(get_current_active_user)]):
    session=get_owned_session(session_id,current_user.username)
    games=get_games_for_session(session_id)


