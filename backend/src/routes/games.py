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
from schemas.game import GameStatus
from utils.rate_limiter import RateLimiter
from uuid import UUID

router = APIRouter(
    prefix="/sessions/{session_id}/games",
    tags=["games"],
    dependencies=[Depends(RateLimiter(times=5, seconds=60))]
)

# POST /sessions/{session_id}/games → creează joc nou
@router.post("", response_model=GameOutput, status_code=status.HTTP_201_CREATED)
async def create_game(
    session_id: str,
    current_user: Annotated[User, Depends(get_current_active_user)],
    db: Session = Depends(get_db)
):
    session_uuid=UUID(session_id)
    existing_game = db.query(GameModel).filter(GameModel.session_id==session_uuid).first()
    word="Ada"
    new_game = GameModel(
        session_id=session_id,
        word=word, 
        pattern="*"*len(word),
        guessed_letters=[],
        wrong_letters=[],
        remaining_misses=6,
        status=GameStatus.IN_PROGRESS
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
    return game.history

# POST /sessions/{session_id}/games/{game_id}/abort → închide joc curent
@router.post("/{game_id}/abort")
async def abort_game(
    session_id: str,
    game_id: str,
    current_user: Annotated[User, Depends(get_current_active_user)],
    db: Session = Depends(get_db)
):
    game = get_owned_game(db, game_id, current_user.user_id)
    if game.status != GameStatus.IN_PROGRESS:
        raise HTTPException(status_code=409,detail="Game already finished")
    game.status = GameStatus.ABORTED
    db.commit()
    db.refresh(game)
    return {"game_id": game.game_id, "status": game.status, "message": "Game aborted with success"}
