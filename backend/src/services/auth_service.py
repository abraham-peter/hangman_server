from sqlalchemy.orm import Session
from models import UserDB
import uuid

def get_user_by_username(db:Session,username:str):
    return db.query(UserDB).filter(UserDB.username== username).first()

def get_user_by_id(db:Session,user_id:str):
    return db.query(UserDB).filter(UserDB.user_id== user_id).first()

