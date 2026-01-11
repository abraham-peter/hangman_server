from sqlalchemy import Column,Integer,String,Boolean,DateTime,ForeignKey,JSON
from sqlalchemy.orm import relationship 
from sqlalchemy.sql import func
from src.database import Base
from services.game_service import generate_uuid

status_game = ["NOT_STARTED", "IN_PROGRESS", "WON", "LOST"]


class UserDB(Base):
    __tablename__="users"

    user_id=Column(Integer,primary_key=True,index=True)
    username=Column(String,unique=True,index=True,nullable=False)
    email=Column(String,unique=True,index=True,nullable=False)
    hashed_password=Column(String,nullable=False)
    is_active=Column(Boolean,default=True)
    created_at=Column(DateTime(timezone=True),server_default=func.now())

    sessions = relationship("Session", back_populates="user")

class Session(Base):
    __tablename__="sessions"

    session_id=Column(String,primary_key=True,default=generate_uuid)
    user_id=Column(Integer,ForeignKey("users.user_id"),nullable=False)
    num_games=Column(Integer,nullable=False)
    params=Column(JSON,nullable=True) # dictionary_id, difficulty, language, max_misses, allow_word_guess, seed # SE POATE IGNORA.
    status=Column(String,default="ACTIVE",nullable=False)
    created_at=Column(DateTime(timezone=True),server_default=func.now())
    finished_at=Column(DateTime(timezone=True),nullable=True)

    user=relationship("UserDB", back_populates="sessions")
    games=relationship("Game",back_populates="session")

class Game(Base):
    __tablename__="games"

    game_id=Column(Integer,primary_key=True,default=generate_uuid)
    session_id=Column(String,ForeignKey("sessions.session_id"),nullable=False)
    word=Column(String,nullable=False)
    pattern=Column(String,nullable=False)
    guessed_letters=Column(JSON,default=list,nullable=False)
    wrong_letters=Column(JSON,default=list,nullable=False)
    remaining_misses=Column(Integer,default=6)
    total_guesses=Column(Integer,default=0)
    status=Column(String,default="IN_PROGRESS")
    result=Column(String,nullable=True)
    created_at=Column(DateTime(timezone=True),server_default=func.now())
    updated_at=Column(DateTime(timezone=True),server_default=func.now(),onupdate=func.now())
    history=Column(JSON,nullable=True, default=list)

    session= relationship("Session",back_populates="games")

    