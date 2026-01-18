from sqlalchemy import Column,Integer,String,Boolean,DateTime,ForeignKey,JSON
from sqlalchemy.orm import relationship 
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from database import Base
from enum import Enum
from sqlalchemy import Enum as SAENum 
from schemas.session import SessionStatus
from schemas.game import GameStatus
import uuid

def generate_uuid():
    return uuid.uuid4()
class UserDB(Base):
    __tablename__="users"

    user_id=Column(Integer,primary_key=True,index=True)
    username=Column(String,unique=True,index=True,nullable=False)
    email=Column(String,unique=True,index=True,nullable=False)
    full_name=Column(String,nullable=True)
    hashed_password=Column(String,nullable=False)
    is_admin=Column(Boolean,default=False,nullable=False)
    is_active=Column(Boolean,default=True)
    created_at=Column(DateTime(timezone=True),server_default=func.now())

    sessions = relationship("Session", back_populates="user")

class Session(Base):
    __tablename__="sessions"

    session_id=Column(UUID(as_uuid=True),primary_key=True,default=generate_uuid)
    user_id=Column(Integer,ForeignKey("users.user_id"),nullable=False)

    dictionary_id=Column(Integer,ForeignKey("dictionaries.id"),nullable=True)
    dictionary=relationship("DictionaryDB")

    num_games=Column(Integer,nullable=False)
    params=Column(JSON,nullable=True) # dictionary_id, difficulty, language, max_misses, allow_word_guess, seed # SE POATE IGNORA.
    status=Column(SAENum(SessionStatus,name="session_status"),default=SessionStatus.ACTIVE,nullable=False)
    created_at=Column(DateTime(timezone=True),server_default=func.now())
    finished_at=Column(DateTime(timezone=True),nullable=True)

    user=relationship("UserDB", back_populates="sessions")
    games=relationship("Game",back_populates="session")

class Game(Base):
    __tablename__="games"

    game_id=Column(UUID(as_uuid=True),primary_key=True,default=generate_uuid)
    session_id=Column(UUID(as_uuid=True),ForeignKey("sessions.session_id"),nullable=False)
    word=Column(String,nullable=False)
    pattern=Column(String,nullable=False)
    guessed_letters=Column(JSON,default=list,nullable=False)
    wrong_letters=Column(JSON,default=list,nullable=False)
    remaining_misses=Column(Integer,default=6)
    total_guesses=Column(Integer,default=0)
    status=Column(SAENum(GameStatus,name="game_status"),default=GameStatus.IN_PROGRESS,nullable=False)
    result=Column(String,nullable=True)
    created_at=Column(DateTime(timezone=True),server_default=func.now())
    updated_at=Column(DateTime(timezone=True),server_default=func.now(),onupdate=func.now())
    history=Column(JSON,nullable=True, default=list)

    session= relationship("Session",back_populates="games")

    @property
    def length(self):
        """Return length of the underlying word."""
        return len(self.word) if self.word else 0

    @property
    def revealed_word(self):
        """Reveal the full word only when the game is finished."""
        if self.status != GameStatus.IN_PROGRESS:
            return self.word
        return None

class DictionaryDB(Base):
    __tablename__ = "dictionaries"
    
    id=Column(Integer,primary_key=True, index=True,nullable=False)
    language=Column(String,index=True,nullable=False) # Aici vine daca-i ro / en
    label=Column(String,nullable=True)
    is_active=Column(Boolean,default=False,nullable=False)

    words=relationship("WordDB",back_populates="dictionary",cascade="all, delete-orphan")

class WordDB(Base):
    __tablename__="words"

    id=Column(Integer,primary_key=True,index=True)
    value=Column(String,index=True)
    dictionary_id=Column(Integer,ForeignKey("dictionaries.id"),nullable=False)

    dictionary=relationship("DictionaryDB",back_populates="words")
