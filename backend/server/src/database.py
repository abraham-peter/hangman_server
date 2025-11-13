from collections.abc import AsyncGenerator
import uuid
from sqlalchemy import Column,String,Text,DateTime,ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.asyncio import AsyncSession,create_async_engine,async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, relationship
from datetime import datetime

DATABASE_URL='sqlite+aiosqlite:///./test.db'

class Base(DeclarativeBase):
    pass

class Post(Base):
    __tablename__ ='posts' #Create a table called posts in the database, and map it to this Python class.
    
    id=Column(UUID(as_uuid=True),primary_key=True,default=uuid.uuid4)
    caption=Column(Text)#id is the primary key (unique for each post),It uses a UUID (universally unique ID) instead of an integer,Its default value will be generated automatically with uuid.uuid4()
    
    url=Column(String,nullable=False)
    file_type=Column(String,nullable=False)
    file_name=Column(String,nullable=False)
    created_at=Column(DateTime,default=datetime.utcnow)
    #example 
    # | id        | caption    | url             | file_type | file_name | created_at       |
    #| --------- | ---------- | --------------- | --------- | --------- | ---------------- |
    #| e8a9d1... | "My photo" | "/images/x.jpg" | "image"   | "x.jpg"   | 2025-11-13 20:00 |
class User(Base):
    __tablename__='User'
    user_id=id=Column(UUID(as_uuid=True),primary_key=True,default=uuid.uuid4)
    
    
    
engine=create_async_engine(DATABASE_URL) #the connection to the database
async_session_maker=async_sessionmaker(engine,expire_on_commit=False) #a factory that creates sessions — sessions are what you use to talk to the database (like “open a conversation with the DB”)
async def create_db_and_tables():
    async with engine.begin() as conn: #engine.begin() starts a connection
        await conn.run_sync(Base.metadata.create_all) # Tells SQLAlchemy Look at all the classes that inherit from DeclarativeBase and create those tables if they don’t exist.
        
async def get_async_session() -> AsyncGenerator[AsyncSession,None]:
    async with async_session_maker() as session: #opens a session safely (it closes automatically)
        yield session #yield means this function is a generator, and since it’s async, it’s an AsyncGenerator
        
    