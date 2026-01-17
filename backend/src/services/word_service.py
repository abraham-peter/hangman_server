import random 
import json
from sqlalchemy.orm import Session
from models import DictionaryDB, WordDB 

LANGUAGE_KEYS = {
    "en": "lista_cuvinte_en",
    "ro": "lista_cuvinte_ro",
}

def import_dictionary_from_json(
        db: Session,
        *,
        language: str,
        json_path: str,
        label: str | None=None
) -> DictionaryDB:
    if language not in LANGUAGE_KEYS:
        raise ValueError("N-avem limba asta Domn Profesor :(")
    
    with open(json_path, "r", encoding="utf-8") as f:
        data=json.load(f)

    key= LANGUAGE_KEYS[language]
    
    if key not in data or not isinstance(data[key], list):
        raise ValueError(f"Invalid JSON, ne lipseste {key}")
    words: list[str]=data[key]
    dictionary= DictionaryDB(
        language=language,
        label=label,
        is_active=False
    )
    db.add(dictionary)
    db.flush() # Datorita dictionary.id

    for w in words:
        db.add(
            WordDB(
                value=w.strip().lower(),
                dictionary_id=dictionary.id
            )
        )
    db.commit()
    db.refresh(dictionary)
    return dictionary

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

    db_words=[WordDB(value=w.strip().lower(),dictionary_id=dictionary.id) for w in words]
    db.add_all(db_words)
    db.commit()
    db.refresh(dictionary)

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
        