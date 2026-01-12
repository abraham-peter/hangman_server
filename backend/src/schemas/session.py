from pydantic import BaseModel
from typing import Union
class SessionCreate(BaseModel):
    num_games: int |None
    dictionary_id: str
    difficulty: str 
    language: str 
    max_misses = int 
    allow_word_guess: bool 
    seed: int | None = None
    
class SessionResponse(BaseModel):
    session_id: str
    num_games: int
    created_at: str
    status: str
class GuessRequest(BaseModel):
    word:str | None
    letter:str |None