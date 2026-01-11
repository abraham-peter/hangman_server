from sqlalchemy import Column,Integer,String,Boolean,DateTime
from sqlalchemy.sql import func
from src.database import Base

class UserDB(Base):
    __tablename__="users"
    user_id=Column(Integer,primary_key=True,index=True)
    username=Column(String,unique=True,index=True,nullable=False)
    email=Column(String,unique=True,index=True,nullable=False)
    hashed_password=Column(String,nullable=False)
    is_active=Column(Boolean,default=True)
    created_at=Column(DateTime(timezone=True),server_default=func.now())

class RegisterUser(Base):
    __tablename__="register"
    username=Column(String,unique=True,index=True,nullable=False)
    email=Column(String,unique=True,index=True,nullable=False)
    password=Column(String,nullable=False)
    #full name optional


    