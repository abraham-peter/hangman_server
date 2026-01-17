from datetime import datetime, timedelta, timezone
import jwt
import uuid
from jwt.exceptions import InvalidTokenError
from fastapi import APIRouter,status,Depends,HTTPException
from typing import Annotated
from fastapi import Response, Depends
from pwdlib import PasswordHash
from schemas.user import User,UserInDB,Token,TokenData,RegisterUser
from models import UserDB
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
from fastapi.security.utils import get_authorization_scheme_param
from starlette.requests import Request
from services.auth_service import get_user_by_id,get_user_by_username
from sqlalchemy.orm import Session
from database import get_db
from middleware.rate_limit import rate_limit

class OAuth2PasswordBearerWithCookie(OAuth2PasswordBearer):
    async def __call__(self, request: Request) -> str | None:
        # Extragem token-ul din cookie
        token: str | None = request.cookies.get("access_token")
        
        scheme, param = get_authorization_scheme_param(token)
        if not token or scheme.lower() != "bearer":
            if self.auto_error:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Not authenticated",
                )
            else:
                return None
        return param

# to get a string like this run:
# openssl rand -hex 32
# -------------------------------------- 
# Config 
# -------------------------------------
SECRET_KEY="739b2d9c01de56d80cec148f3b1bd7c37959b83fa122bb07b7ab284d1500f751"
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=30

router=APIRouter()
password_hash = PasswordHash.recommended()
oauth2_scheme=OAuth2PasswordBearer(tokenUrl="auth/login")
def verrify_password(plain_password:str,hashed_password:str):
    return password_hash.verify(plain_password,hashed_password)

def get_hash_password(password: str):
    return password_hash.hash(password)

def get_user(db,username:str):
    if username in db:
        user_dict=db[username]
        return UserInDB(**user_dict)
def get_user_by_id(db, user_id: str):
    for user_data in db.values():
        if user_data.get("user_id") == user_id:
            return UserInDB(**user_data)
    return None

def authenticate_user(db:Session,username:str,password:str) -> UserInDB | None:
    user=get_user_by_username(db,username)
    if not user:
        return False
    if not verrify_password(password,user.hashed_password):
        return False
    return user
def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# DEPENDENCIES
async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)],
                           db:Session=Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("sub")  
        if user_id is None:
            raise credentials_exception
        token_data = TokenData(username=user_id)  
    except InvalidTokenError:
        raise credentials_exception
    user = get_user_by_id(db, user_id)  
    if user is None:
        raise credentials_exception
    return user
async def get_current_active_user(
    current_user: Annotated[User, Depends(get_current_user)],
):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

    

@router.post("/auth/register", status_code=status.HTTP_200_OK, response_model=User)
async def register_user(register: RegisterUser,db:Session=Depends(get_db)):
    db_user=get_user_by_username(db,register.username)
    if db_user:
        raise HTTPException(status_code=400,detail="Username already exists")
    

    hashed_password = get_hash_password(register.password)
    
    user_in_db = UserDB( 
        username=register.username,
        full_name=register.full_name,
        email=register.email,
        hashed_password=hashed_password,
        is_active=True,
    )
    db.add(user_in_db)
    db.commit()
    db.refresh(user_in_db)
    
    return user_in_db
@router.post("/auth/login", status_code=status.HTTP_201_CREATED, response_model=Token,dependencies=[Depends(rate_limit(5, 60))])  
async def login_for_access_token(
    response:Response,
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db:Session=Depends(get_db)
) -> dict[str,str]: 
    user = get_user_by_username(db,form_data.username)
    if not user or not verrify_password(form_data.password,user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": str(user.id)}, expires_delta=access_token_expires  
    )
    response.set_cookie(
        key="access_token",
        value=f"Bearer {access_token}",
        httponly=True,
        max_age=ACCESS_TOKEN_EXPIRE_MINUTES*60,
        samesite="lax",
        secure=True,

    )
    return {"messsage":"Logged in succesfully"}

@router.post("/auth/logout")
async def logout(response: Response):
    response.delete_cookie("access_token")
    return {"message": "Logged out"}
    


@router.post("/auth/refresh", status_code=status.HTTP_200_OK)
async def refresh_token(current_user: Annotated[UserDB, Depends(get_current_active_user)]):
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    new_token = create_access_token(
        data={"sub": str(current_user.id)}, expires_delta=access_token_expires
    )
    return {"access_token": new_token, "token_type": "bearer"}


@router.get("/users/me",response_model=User,status_code=status.HTTP_200_OK)
async def read_user_me(current_user:Annotated[User,Depends(get_current_active_user)]):
    return current_user
