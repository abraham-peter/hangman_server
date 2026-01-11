from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
from hangman_server.backend.src.models import UserDB

SQLALCHEMY_DATABASE_URL="postgresql://postgres:9GL7q8eNEf9c@localhost:5432/fastapi_db"

engine=create_engine(SQLALCHEMY_DATABASE_URL)

Session_Local=sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base=declarative_base()
UserDB.Base.metadata.create_all(bind=engine)

def get_db():
    db=Session_Local()
    try:
        yield db
    finally:
        db.close()