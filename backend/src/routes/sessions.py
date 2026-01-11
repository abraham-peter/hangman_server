from fastapi import APIRouter,HTTPException,Depends,status
from routes.auth import get_current_active_user
from schemas.user import User
from schemas.session import SessionResponse, SessionCreate
from schemas.session import GuessRequest
from schemas.game import GameOutput
from services.game_service import apply_guess, get_owned_game
from typing import Annotated
import uuid
from sqlalchemy.orm import Session
from database import get_db
from models import Game
from models import Session
from utils.rate_limiter import RateLimiter

router = APIRouter(
    prefix="/sessions",
    tags=["sessions"],
    dependencies=[Depends(RateLimiter(times=5, seconds=60))]
)
# POST /sessions -> Creeaza sesiune noua
@router.post("", response_model=SessionResponse, status_code=status.HTTP_201_CREATED)
async def create_session(session_data: SessionCreate,  # aici pui schema Pydantic pentru request
                         current_user: Annotated[User, Depends(get_current_active_user)],
                         db: Session = Depends(get_db)):
    new_session= Session(
        user_id=current_user.user_id,
        num_games=session_data.num_games,
        dictionary_id=session_data.dictionary_id,
        difficulty=session_data.difficulty,
        language=session_data.language,
        max_misses=session_data.max_misses,
        allow_word_guess=session_data.allow_word_guess,
        seed=session_data.seed, 
        status="ACTIVE"
    )
    db.add(new_session)
    db.commit()
    db.refresh(new_session)
    return new_session

# GET /sessions/{sesion_id} -> DETALII SESIUNE
@router.get("/{session_id}", response_model=SessionResponse)
async def get_session(
    session_id: str,
    current_user: Annotated(User, Depends(get_current_active_user)),
    db: Sesssion = Depends(get_db),
):
    session = db.query(Session).filter_by(session_id=session_id).first()
    if not session or session.user_id != current_user.user_id:
        raise HTTPException(status_code=404, detail= "Session not found or not owned by user")
    return session

# POST /sesssions/{session_id}/abort -> inchide sesiunea 
@router.post("/{session_id}/abort", status_code=status.HTTP_200_OK)
async def abort_session(
    session_id: str,
    current_user: Annotated(User, Depends(get_current_active_user)),
    db: Session = Depends(get_db)
):
    session=db.query(Session).filter_by(session_id=session_id).first()
    if not session or session.user_id != current_user.user_id:
        raise HTTPException(status_code=404, detail="Session not found or not owned by user")
    if session.status != "ACTIVE":
        raise HTTPException(status_code=409, detail="Session already finished")
    session.status= "ABORTED"
    db.commit()
    db.refresh(session)
    return {"session_id": session.session_id, "status": session.status, "message": "Session aborted with success"}

# GET /sessions/{session_id}/games -> Lista jocuri
@router.get("/{session_id}/games")
async def list_games(
    session_id: str,
    current_user: Annotated[User, Depends(get_current_active_user)],
    db: Session = Depends(get_db)
):
    session = db.query(SessionModel).filter_by(session_id=session_id).first()
    if not session or session.user_id != current_user.user_id:
        raise HTTPException(status_code=404, detail="Session not found or not owned by user")
    games = db.query(GameModel).filter_by(session_id=session_id).all()
    return games

# GET /sessions/{session_id}/stats -> Statisticile
@router.get("/{session_id}/stats")
async def session_stats(
    session_id: str,
    current_user: Annotated[User, Depends(get_current_active_user)],
    db: Session = Depends(get_db)
):
    session = db.query(SessionModel).filter_by(session_id=session_id).first()
    if not session or session.user_id != current_user.user_id:
        raise HTTPException(status_code=404, detail="Session not found or not owned by user")
    games = db.query(GameModel).filter_by(session_id=session_id).all()
    total=len(games)
    finished=sum(1 for g in games if g.status in ["WON", "LOST"])
    wins=sum(1 for g in games if g.status=="WON")
    losses=sum(1 for g in games if g.status=="LOST")
    avg_guesses = sum(g.total_guesses for g in games)/total if total else 0
    avg_wrong = sum(len(g.wrong_letters) for g in games)/total if total else 0
    return {
        "session_id": session_id,
        "games_total": total,
        "games_finished": finished,
        "wins": wins,
        "losses": losses, 
        "avg_total_guesses": avg_guesses,
        "avg_wrong_letters": avg_wrong
    }