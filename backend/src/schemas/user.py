from pydantic import BaseModel,EmailStr
from fastapi_users import schemas
import uuid
class User(BaseModel):# ce trimitem inapoi in frontend
    user_id:str
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None
    
class Token(BaseModel):
    acces_token:str
    token_type:str

class TokenData(BaseModel):
    username:str | None=None
    
class UserInDB(User):#ce se passtreaza in db
    user_id:str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None
    hashed_password:str
class RegisterUser(BaseModel):#ce cerem de la user temporar 
    username:str
    full_name:str
    email:EmailStr
    password:str
class LoginUser(BaseModel):
    email:EmailStr
    password:str
    