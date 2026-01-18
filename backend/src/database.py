from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
from dotenv import load_dotenv
import os
load_dotenv()


SQLALCHEMY_DATABASE_URL = os.getenv("SQLALCHEMY_DATABASE_URL")
if not SQLALCHEMY_DATABASE_URL:
    # fallback for minimal local development
    SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

# Older Render/Heroku style postgres urls use "postgres://" which SQLAlchemy expects "postgresql://"
if SQLALCHEMY_DATABASE_URL and SQLALCHEMY_DATABASE_URL.startswith("postgres://"):
    SQLALCHEMY_DATABASE_URL = SQLALCHEMY_DATABASE_URL.replace("postgres://", "postgresql://", 1)

# Use sqlite connect args when applicable
if SQLALCHEMY_DATABASE_URL.startswith("sqlite"):
    engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
else:
    engine = create_engine(SQLALCHEMY_DATABASE_URL)

Session_Local=sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base=declarative_base()
Base.metadata.create_all(bind=engine)
def get_db():
    db=Session_Local()
    try:
        yield db
    finally:
        db.close()