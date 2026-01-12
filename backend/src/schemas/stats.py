from pydantic import BaseModel

class PostCreate(BaseModel):
    session_id: str | None
    games_total: str | None
    game_finished: str | None
    wins: int | None
    losses: int | None
    avg_total_guesses: int | None
    avg_wrong_letters: int | None
    avg_time_sec: int | None
    composite_score: int | None

class PostResponse(BaseModel):
    session_id: str | None
    games_total: str | None
    game_finished: str | None
    wins: int | None
    losses: int | None
    avg_total_guesses: int | None
    avg_wrong_letters: int | None
    avg_time_sec: int | None
    composite_score: int | None