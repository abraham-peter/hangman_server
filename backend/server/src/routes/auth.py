from backend.server.src.app.app import *
from fastapi import APIRouter,HTTPException
from pydantic import BaseModel
from services.auth_service import hash_password,verify_password,create_acces_token
router=APIRouter()

class User(BaseModel):
    email:str
    password:str
    nickname:str

class LoginRequest(BaseModel):
    email:str
    password:str
   
@app.put("/login")
async def autentification():
    pass