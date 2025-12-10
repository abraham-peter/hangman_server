from pydantic import BaseModel

class PostCreate:
    game_id:str | None
    session_id:str | None
    status: str | None 
    lenght: int | None
    pattern: str | None
    guessed_letters: list[str] | None
    wrong_letters: list[str] | None
    remaning_misses: int | None
    total_guesses: int | None
    result: None

class PostResponse:
    game_id:str | None
    session_id:str | None
    status: str | None
    lenght: int | None
    pattern: str | None
    guessed_letters: list[str] | None
    wrong_letters: list[str] | None
    remaning_misses: int | None
    total_guesses: int | None
    result: None
   
    