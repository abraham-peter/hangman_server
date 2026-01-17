from fastapi import APIRouter, Depends, Query, status, HTTPException
from sqlalchemy.orm import Session 
from sqlalchemy import func, case
from datetime import datetime, timedelta
from models import GameStatus, UserDB
from models import Game as GameDB

def session_stats(games: list[GameDB]):
    finished=0
    wins=0
    losses=0
    total_guesses=0
    total_wrong=0
    for g in games:
        if g.status in (GameStatus.WON, GameStatus.LOST):
            finished+=1
            total_guesses+=g.total_guesses or 0
            total_wrong+=len(g.wrong_letters or [])
            if g.status==GameStatus.WON:
                wins+=1
            else:
                losses+=1
    win_rate=wins/finished if finished else 0
    avg_guesses=total_guesses / finished if finished else 0
    avg_wrong=total_wrong / finished if finished else 0

    return{
        "games_total":len(games),
        "games_finished":finished,
        "wins":wins,
        "losses":losses,
        "win_rate":round(win_rate,3),
        "avg_total_guesses":round(avg_guesses,2),
        "avg_wrong_letters":round(avg_wrong,2),
    } 

def period_to_datetime(period:str|None):
    if period in (None,"all"):
        return None 
    if period=="30d":
        return datetime.utcnnow() - timedelta(days=30)
    if period=="7d":
        return datetime.utcnnow() - timedelta(days=7)
    if period=="1d":
        return datetime.utcnnow() - timedelta(days=1)
    raise HTTPException(status_code=400, detail="Invalid period")

def composite_score_expr():
    """
    S_joc = 1000 * won
          - 10 * total_guesses
          - 5  * wrong_letters
          - 40 * wrong_word_guesses
          - 0.2 * time_sec
          + 2  * length
    """
    return (
        1000 * case((GameDB.status == GameStatus.WON, 1), else_=0)
        - 10 * GameDB.total_guesses
        - 5 * func.json_array_length(GameDB.wrong_letters)
        - 40 * GameDB.wrong_word_guesses
        - 0.2 * GameDB.time_sec
        + 2 * GameDB.length
    )