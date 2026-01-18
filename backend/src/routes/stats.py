from fastapi import APIRouter,status,Depends,HTTPException, Query
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import Annotated 
from database import get_db 
from middleware.rate_limit import RateLimiter
from routes.auth import get_current_active_user
from schemas.user import User
from schemas.game import GameStatus
from models import UserDB, Session as SessionDB, Game 
from services.stats_service import period_to_datetime, composite_score_expr, session_stats

router=APIRouter(
    prefix="/stats",
    tags=["stats"],
    dependencies=[Depends(RateLimiter(times=10, seconds=60))])


@router.get("/users/{user_id}", status_code=status.HTTP_200_OK)
async def user_stats(
    user_id: int,
    current_user: Annotated[User, Depends(get_current_active_user)],
    db: Session = Depends(get_db),
    period: str | None = Query(default="all")
):
    if current_user.user_id != user_id:
        raise HTTPException(status_code=403, detail="Access DENIED :(")
    since=period_to_datetime(period)


    sessions = db.query(SessionDB).filter(SessionDB.user_id == user_id).all()
    if not sessions:
        return {
            "user_id": user_id,
            "sessions":0,
            "games":0,
            "wins":0,
            "losses":0,
            "win_rate":0.0,
            "avg_guesses":0.0,
            "avg_wrong_letters":0.0
        }
    session_ids=[s.session_id for s in sessions]

    q=db.query(Game).filter(Game.session_id.in_(session_ids))
    if since:
        q=q.filter(Game.created_at>=since)

    games=q.all()
    stats=session_stats(games)

    return {
        "user_id": user_id,
        "sessions": len(sessions),
        **stats
    }

@router.get("/global", status_code=status.HTTP_200_OK)
async def global_stats(period: str | None=Query(default="all"),db:Session=Depends(get_db)):
    since=period_to_datetime(period)
    q=db.query(Game)
    if since:
        q=q.filter(Game.created_at >=since)

    games=q.all()
    stats=session_stats(games)
    return stats

@router.get("/leaderboard", status_code=status.HTTP_200_OK)
async def leaderboard(
    limit: int= Query(default=100,le=500),
    db: Session = Depends(get_db)
):  
    leaderboard_query = (
        db.query(
            UserDB.user_id,
            UserDB.username,
            func.count(Game.id).label("games"),
            func.sum(func.case((Game.status == "WON", 1), else_=0)).label("wins"),
            func.sum(func.case((Game.status == "LOST", 1), else_=0)).label("losses"),
            func.avg(Game.total_guesses).label("avg_guesses"),
            func.avg(func.json_array_length(Game.wrong_letters)).label("avg_wrong_letters"),
            func.avg(composite_score_expr()).label("score")
        )
        .join(SessionDB, SessionDB.user_id==UserDB.user_id)
        .join(Game, Game.session_id==SessionDB.session_id)
        .group_by(UserDB.user_id)
        .order_by(func.avg(composite_score_expr()).desc())
        .limit(limit)
    )
    result=leaderboard_query.all()


    leaderboard=[]
    for r in result:
        win_rate= r.wins / r.games if r.games else 0
        leaderboard.append({
            "user_id": r.user_id,
            "username": r.username,
            "games": r.games,
            "wins": r.wins,
            "losses": r.losses,
            "win_rate": round(win_rate, 3),
            "avg_guesses": round(r.avg_guesses or 0, 2),
            "avg_wrong_letters": round(r.avg_wrong_letters or 0, 2),
            "score": round(r.score, 2)
        })
    return leaderboard