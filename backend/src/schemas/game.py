from pydantic import BaseModel
status_game=["NOT_STARTED","IN_PROGRESS","WON","LOST"]
fake_db_word="Ada"

class GameStats(BaseModel):
    game_id:str | None
    session_id:str | None
    status: str=status_game[0]
    lenght: int=len(fake_db_word)+1
    pattern: str="*"*(len(fake_db_word)+1)
    guessed_letters: list[str]=[]
    wrong_letters: list[str]=[]
    remaning_misses: int=5
    total_guesses: int=0
    result: None

class GameOutput(BaseModel):
    pattern: str | None
    guessed_letters: list[str] | None
    wrong_letters: list[str] | None
    remaning_misses: int | None
    status:str
   
    