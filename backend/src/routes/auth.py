from datetime import datetime, timedelta, timezone
import jwt
import uuid
from jwt.exceptions import InvalidTokenError
from fastapi import APIRouter,status,Form,Depends,HTTPException
from typing import Annotated
from schemas.auth import FormData
from pwdlib import PasswordHash
from schemas.user import User,UserInDB,Token,TokenData,RegisterUser
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm

# to get a string like this run:
# openssl rand -hex 32
SECRET_KEY="739b2d9c01de56d80cec148f3b1bd7c37959b83fa122bb07b7ab284d1500f751"
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=30
fake_users_db = {
    "johndoe": {
        "user_id": str(uuid.uuid4()), 
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "$argon2id$v=19$m=65536,t=3,p=4$wagCPXjifgvUFBzq4hqe3w$CYaIb8sB+wtD+Vu/P4uod1+Qof8h+1g7bbDlBID48Rc",
        "disabled": False,
    }
}

password_hash = PasswordHash.recommended()
router=APIRouter()
oauth2_scheme=OAuth2PasswordBearer(tokenUrl="token")
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

def authenticate_user(fake_db,username:str,password:str):
    user=get_user(fake_db,username)
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
async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
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
    user = get_user_by_id(fake_users_db, user_id)  
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
async def register_user(register: RegisterUser):
    if register.username in fake_users_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already exists"
        )
    
    user_id = str(uuid.uuid4())  
    hashed_password = get_hash_password(register.password)
    
    user_in_db = UserInDB(
        user_id=user_id,  
        username=register.username,
        full_name=register.full_name,
        email=register.email,
        hashed_password=hashed_password,
        disabled=False,
    )
    
    fake_users_db[register.username] = user_in_db.model_dump()
    
    return User(
        user_id=user_in_db.user_id,
        username=user_in_db.username,
        full_name=user_in_db.full_name,
        email=user_in_db.email,
        disabled=user_in_db.disabled,
    )
@router.post("/auth/login", status_code=status.HTTP_201_CREATED, response_model=Token)  
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
) -> Token:
    user = authenticate_user(fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.user_id}, expires_delta=access_token_expires  
    )
    return Token(access_token=access_token, token_type="bearer")
    


@router.post("/auth/refresh",status_code=status.HTTP_200_OK)


@router.get("/users/me",response_model=User,status_code=status.HTTP_201_CREATED)
async def read_user_me(current_user:Annotated[User,Depends(get_current_active_user)]):
    return current_user
