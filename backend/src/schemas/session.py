from pydantic import BaseModel
from typing import Union
class PostCreate(BaseModel):
    session_id: str | None
    user_id: str | None
    num_games: int |None
    params: dict[str, Union[str,int,bool]]
    status: str | None
    created_at: str | None
    finished_at: None
    
class PostResponse(BaseModel):
    user_id:str | None
    email:str | None
    nickname: str |None