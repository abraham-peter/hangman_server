import random 
from sqlalchemy.orm import Session
from models import DictionaryDB, WordDB 

def get_all_dictionaries(db:Session):
    return db.query(DictionaryDB).all()

def create_dictionary(db: Session, language: str, label: str | None, words: list[str]):
    dictionary=DictionaryDB(
        language=language,
        label=label,
        is_active=False
    )
    db.add(dictionary)
    db.commit()
    db.refresh(dictionary)

    db_words=[WordDB(value=w,dictionary_id=dictionary.id) for w in words]
    db.add_all(db_words)
    db.commit()

    return dictionary

def update_dictionary(db:Session,dictionary_id:int,is_active=None,label=None):
    dictionary= db.query(DictionaryDB).filter(DictionaryDB.id==dictionary_id).first()
    if not dictionary:
        return None 
    if is_active is not None:
        dictionary.is_active=is_active
    if label is not None: 
        dictionary.label=label 

    db.commit()
    db.refresh(dictionary)
    return dictionary 

def get_dictionary_sample(db:Session,dictionary_id:int,sample:int):
    words=(
        db.query(WordDB)
        .filter(WordDB.dictionary_id==dictionary_id)
        .all()
    )
    if not words:
        return []
    
    return random.sample(words,min(sample,len(words)))
        