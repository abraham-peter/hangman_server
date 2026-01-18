from fastapi import APIRouter,HTTPException, status, Depends,Query
from sqlalchemy.orm import Session
from typing import Annotated
from database import get_db
from models import UserDB 
from schemas.dictionary import DictionaryCreate, DictionaryOut, DictionaryPatch
from services.word_service import get_all_dictionaries, create_dictionary, update_dictionary, get_dictionary_sample
from routes.auth import get_current_active_user

def admin_required(user: UserDB):
    if not user.is_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Asta este Admin Panel :("
        )

router=APIRouter(prefix="/admin/dictionaries",tags=["Admin Dictionaries"])

@router.get("", response_model=list[DictionaryOut])
def list_dictionaries(current_user:Annotated[UserDB, Depends(get_current_active_user)], db: Session = Depends(get_db)):
    admin_required(current_user)
    return get_all_dictionaries(db)

@router.post("", response_model=DictionaryOut, status_code=status.HTTP_201_CREATED)
def import_dictionary(data: DictionaryCreate, current_user: Annotated[UserDB, Depends(get_current_active_user)], db:Session=Depends(get_db)):
    admin_required(current_user)
    return create_dictionary(db,data.language,data.label,data.words)

@router.patch("/{dictionary_id}", response_model=DictionaryOut)
def patch_dictionary(dictionary_id: int, data: DictionaryPatch, current_user: Annotated[UserDB,Depends(get_current_active_user)], db:Session=Depends(get_db)):
    admin_required(current_user)
    dictionary=update_dictionary(
        db,
        dictionary_id,
        is_active=data.is_active,
        label=data.label,
    )
    if not dictionary:
        raise HTTPException(status_code=404,detail="Dictionary not found")
    return dictionary 

@router.get("/{dictionary_id}/words")
def dictionary_sample(
    dictionary_id: int,
    sample: int=20,
    current_user= Annotated[UserDB,Depends(get_current_active_user)],
    db:Session=Depends(get_db)
):
    admin_required(current_user)
    words=get_dictionary_sample(db,dictionary_id,sample)
    return [w.value for w in words]