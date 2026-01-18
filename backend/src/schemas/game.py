from pydantic import BaseModel
from typing import Optional
from enum import Enum

class GameOutput(BaseModel):
    game_id: str
    session_id: str
    pattern: str
    length: int
    revealed_word: Optional[str] = None
    guessed_letters: list[str]
    wrong_letters: list[str]
    remaining_misses: int
    status: str
    total_guesses: int
    result: Optional[str] = None
    class Config:
        from_attributes=True
    
class GameStatus(str, Enum):
    NOT_STARTED ="NOT_STARTED"
    IN_PROGRESS="IN_PROGRESS"
    WON="WON"
    LOST="LOST"
    ABORTED="ABORTED"

class GameStats(BaseModel):
    game_id:str
    session_id:str
    status: str=GameStatus.IN_PROGRESS # NEEDS CHECKING (TREBE NEAPARAT)
    length: int=0
    pattern: str=""
    guessed_letters: list[str]=[]
    wrong_letters: list[str]=[]
    remaining_misses: int=5
    total_guesses: int=0
    result: str | None = None