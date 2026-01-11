from sqlalchemy import Column,Integer,String,Boolean,DateTime,ForeignKey,JSON
from sqlalchemy.orm import relationship 
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
class Session(Base):
    __tablename__="sessions"
    session_id=Column(Integer,primary_key=True,index=True)
    user_id=Column(Integer,ForeignKey("users.user_id"),nullable=False)
    num_games=Column(Integer,default=0)
    params=Column(JSON,nullable=True)
    status=Column(String,default="ACTIVE")
    created_at=Column(DateTime(timezone=True),server_default=func.now())
    finished_at=Column(DateTime(timezone=True),nullable=True)
    games=relationship("Game",backref="session")
class Game(Base):
    __tablename__="games"
    game_id=Column(Integer,primary_key=True,index=True)
    session_id=Column(ForeignKey("sessions.session_id"),nullable=False)
    word=Column(String,nullable=False)
    pattern=Column(String,nullable=False)
    guessed_letters=Column(JSON,default=list)
    wrong_letters=Column(JSON,default=list)
    remaining_misses=Column(Integer,nullable=False)
    status=Column(String,default="IN_PROGRESS")
    created_at=Column(DateTime(timezone=True),server_default=func.now())
    finished_at=Column(DateTime(timezone=True),nullable=True)

    