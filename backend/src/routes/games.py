from fastapi import APIRouter,HTTPException,Depends,status
from routes.auth import get_current_active_user
from schemas.user import User
from schemas.session import GuessRequest
from schemas.game import GameOutput
from services.game_service import apply_guess,record_history,abort_game,playable_in_guess
from typing import Annotated
import uuid
router=APIRouter()
def get_owned_game(session_id:str,game_id:str,user_id:str):
    session=fake_session_db[session_id]
    if not session:
        raise KeyError("Session_not_found")
    if session["user_id"]!=user_id:
        raise PermissionError("Not your session")
    game=session["games"]
    if not game:
        raise KeyError("Game not found")
    return game
fake_session_db={}
Game = {
    "game_id": "g_123",
    "session_id": "s_456",
    "user_id": "u_1",
    "word": "ada",
    "pattern": "***",
    "guessed_letters": set(),
    "wrong_letters": set(),
    "remaining_misses": 6,
    "status": "IN_PROGRESS",
    "history": [],
}

    
@router.post("/sessions")
async def sessions(
    current_user:Annotated[User,Depends(get_current_active_user)]
    ):
    session_id=str(uuid.uuid4())
    game_id=str(uuid.uuid4())
    fake_session_db[session_id]={
        "user_id":current_user.user_id,
        "games":{
            game_id:{
                "game_id":game_id,
                "session_id":session_id,
                "user_id":current_user.user_id,
                "word":"ada",
                "pattern":"***",
                "guessed_letters":set(),
                "wrong_letters":set(),
                "remaning_misses":6,
                "status":"IN_PROGRESS",
            }
        }
    }
    return {"session_id":session_id,
            "game_id":game_id}

@router.get("/sessions/{session_id}")
async def get_session(session_id:str, 
                      current_user:Annotated[User,Depends(get_current_active_user)]
                      ):
    session=fake_session_db[session_id]
    if not session:
        raise HTTPException(status_code=404,detail="Session not found")
    if session["owner"]!=current_user.username:
        raise HTTPException(status_code=403,detail="Not your session")
    masked_word=[]
    for letter in session["word"]:
        if letter in session["guessed_letters"]:
            masked_word.append(letter)
        else:
            masked_word.append("_")
    return {
        "session_id":session_id,
        "games":list(session["games"].keys())
    }


@router.post("/sessions/{session_id}/games/{game_id}/guess")
async def guess (
    session_id:str,
    game_id:str,
    guess:GuessRequest,
    current_user:Annotated[User,Depends(get_current_active_user)],
):
    try:
        game=get_owned_game(session_id,game_id,current_user.user_id)
        updated_game=apply_guess(game,guess)
        playable_in_guess(game)
        return{
            "game_id":game_id,
            "status":updated_game["status"],
            "pattern":updated_game["pattern"],
            "remaining_misses":updated_game["remaining_misses"],
            "guessed_letters":updated_game["guessed_letters"],
            "wrong_letters":list(updated_game["wrong_letters"]),
        }
    except ValueError as e:
        raise HTTPException(
            status_code=422,
            detail=str(e),
        )
    



@router.get("/sessions/{session_id}/games/{game_id}/state",
            response_model=GameOutput,
            status_code=status.HTTP_200_OK,)
async def state(current_user:Annotated[User,Depends(get_current_active_user)],
                session_id:str,
                game_id:str,
                ):
    try:
        game=get_owned_game(session_id,game_id,current_user.user_id)

        record_history(game)

        return GameOutput(
            pattern=game["pattern"],
            remaining_misses=game["remaining_misses"],
            guessed_letters=game["guessed_letters"],
            wrong_letters=list(game["wrong_letters"]),
            status=game["status"]
        )
    except PermissionError:
        raise HTTPException(status_code=403,detail="Forbidden")
    except KeyError as e:
        raise HTTPException(status_code=404,detail="Game not found")


@router.get("/sessions/{session_id}/games/{game_id}/history",
            status_code=status.HTTP_200_OK)
async def hystory(current_user:Annotated[User,Depends(get_current_active_user)],
                session_id:str,
                game_id:str,):
    try:
        game=get_owned_game(session_id,game_id,current_user.user_id)
        return game["history"]
    except PermissionError:
        raise HTTPException(status_code=403,detail="Forbidden")
    except KeyError as e:
        raise HTTPException(status_code=404,detail="Game not found")


@router.post("/sessions/{session_id}/games/{game_id}/abort",
             status_code=status.HTTP_200_OK,)
async def abort(current_user:Annotated[User,Depends(get_current_active_user)],
                session_id:str,
                game_id:str,):
    try:
        game= game=get_owned_game(session_id,game_id,current_user.user_id)
        abort_game(game)
        record_history(game)
        return{
            "game_id":game_id,
            "status":game["status"],
            "message":"Game aborted succesfully",
        }
    except ValueError:
        raise HTTPException(
            status_code=409,
            detail="Game is already finished",
        )
    except PermissionError:
        raise HTTPException(status_code=403,detail="Forbidden")
    except KeyError as e:
        raise HTTPException(status_code=404,detail="Game not found")

