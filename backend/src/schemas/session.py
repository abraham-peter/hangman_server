from pydantic import BaseModel
from typing import Optional
from typing import Union
from enum import Enum
from sqlalchemy import Enum as SAEEnum
class SessionCreate(BaseModel):
    num_games: int |None
    dictionary_id: str
    difficulty: str 
    language: str 
    max_misses: int
    allow_word_guess: bool 
    seed: int | None = None
    
class SessionResponse(BaseModel):
    session_id: str
    num_games: int
    created_at: str
    status: str

    class Config:
        from_attributes=True
class GuessRequest(BaseModel):
    word:str | None
    letter:str |None

class SessionStatus(str,Enum):
    ACTIVE="ACTIVE"
    ABORTED="ABORTED"
    FINISHED="FINISHED"

