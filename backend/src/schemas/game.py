from pydantic import BaseModel
from typing import Optional
status_game=["NOT_STARTED","IN_PROGRESS","WON","LOST"]

class GameStats(BaseModel):
    game_id:str | None
    session_id:str | None
    status: str= "IN_PROGRESS"
    lenght: int=0
    pattern: str=""
    guessed_letters: list[str]=[]
    wrong_letters: list[str]=[]
    remaining_misses: int=5
    total_guesses: int=0
    result: str | None = None

class GameOutput(BaseModel):
    game_id: str
    session_id: str
    pattern: str
    guessed_letters: list[str]
    wrong_letters: list[str]
    remaining_misses: int
    status: str
    total_guesses: int
    result: Optional[str] = None
    