from pydantic import BaseModel

class PostCreate:
    game_id: str | None
    index: int | None
    type: str | None
    value: str | None
    correct: bool | None
    pattern_after:bool | None
    timestamp: str | None

class PostResponse:
    game_id: str | None
    index: int | None
    type: str | None
    value: str | None
    correct: bool | None
    pattern_after:bool | None
    timestamp: str | None
    