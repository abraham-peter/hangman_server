from pydantic import BaseModel,EmailStr
from fastapi_users import schemas
import uuid
class PostCreate(BaseModel):
    user_id:str | None
    email:EmailStr
    nickname: str |None
    created_at: str | None
    
class PostResponse(BaseModel):
    user_id:str | None
    email:EmailStr
    nickname: str | None
    created_at: str | None

    
class UserRead(schemas.BaseUser[uuid.UUID]):
    pass

class UserCreate(schemas.BaseUserCreate):
    pass

class UserUpdate(schemas.BaseUserUpdate):
    pass
    