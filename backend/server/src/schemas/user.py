from pydantic import BaseModel

class PostCreate(BaseModel):
    user_id:str | None
    email:str | None
    nickname: str |None
    created_at: str | None
    
class PostResponse(BaseModel):
    user_id:str | None
    email:str | None
    nickname: str | None
    created_at: str | None
    