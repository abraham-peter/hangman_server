from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from typing import Annotated
from schemas.user import User
from routes.auth import get_current_active_user
from schemas.session import GuessRequest
from schemas.game import GameOutput
from services.game_service import apply_guess, get_owned_game
from database import get_db
from models import Game as GameModel
from utils.rate_limiter import RateLimiter
import uuid

router = APIRouter(
    prefix="/sessions/{session_id}/games",
    tags=["games"],
    dependencies=[Depends(RateLimiter(times=5, seconds=60))]
)

<<<<<<< HEAD
    
@router.post("/sessions")
async def sessions(
    current_user:Annotated[User,Depends(get_current_active_user)],
    db:Session=(get_db)
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
    session_id:int,
    game_id:int,
    guess:GuessRequest,
    current_user:Annotated[User,Depends(get_current_active_user)],
    db:Session=Depends(get_db),
=======
# POST /sessions/{session_id}/games → creează joc nou
@router.post("", response_model=GameOutput, status_code=status.HTTP_201_CREATED)
async def create_game(
    session_id: str,
    current_user: Annotated[User, Depends(get_current_active_user)],
    db: Session = Depends(get_db)
>>>>>>> 740381c2401b1910c7ae8751e20ce42b210f5605
):
    word="Ada"
    new_game = GameModel(
        session_id=session_id,
        word=word 
        pattern="*"*len(word),
        guessed_letters=[],
        wrong_letters=[],
        remaining_misses=6
        status="IN_PROGRESS"
    )
    db.add(new_game)
    db.commit()
    db.refresh(new_game)
    return new_game

# GET /sessions/{session_id}/games/{game_id}/state → starea jocului
@router.get("/{game_id}/state", response_model=GameOutput)
async def get_game_state(
    session_id: str,
    game_id: str,
    current_user: Annotated[User, Depends(get_current_active_user)],
    db: Session = Depends(get_db)
):
    game = get_owned_game(db,game_id,current_user.user_id)
    return game 

# POST /sessions/{session_id}/games/{game_id}/guess → ghicire literă sau cuvânt
@router.post("/{game_id}/guess", response_model=GameOutput)
async def guess_game(
    session_id: str,
    game_id: str,
    guess: GuessRequest,
    current_user: Annotated[User, Depends(get_current_active_user)],
    db: Session = Depends(get_db)
):
    game=get_owned_game(db,game_id,current_user.user_id)
    try:
        apply_guess(game, guess.letter or guess.word)
        db.commit()
        db.refresh(game)
        return game 
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))
    
# GET /sessions/{session_id}/games/{game_id}/history → istoric ghiciri
@router.get("/{game_id}/history")
async def game_history(
    session_id: str,
    game_id: str,
    current_user: Annotated[User, Depends(get_current_active_user)],
    db: Session = Depends(get_db)
):
    game = get_owned_game(db, game_id, current_user.user_id)

# POST /sessions/{session_id}/games/{game_id}/abort → închide joc curent
@router.post("/{game_id}/abort")
async def abort_game(
    session_id: str,
    game_id: str,
    current_user: Annotated[User, Depends(get_current_active_user)],
    db: Session = Depends(get_db)
):
    game = get_owned_game(db, game_id, current_user.user_id)
    if game.status not in ["IN_PROGRESS"]:
        raise HTTPException(status_code=409,detail="Game already finished")
    game.status = "ABORTED"
    db.commit()
    db.refresh(game)
    return {"game_id": game.game_id, "status": game.status, "message": "Game aborted with success"}
