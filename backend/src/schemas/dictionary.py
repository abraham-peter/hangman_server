from pydantic import BaseModel
from typing import List, Optional

class DictionaryOut(BaseModel):
    id: int
    language: str
    label: Optional[str]
    is_active: bool 
    
    class Config:
        from_attributes=True

class DictionaryCreate(BaseModel):
    language: str
    label: Optional[str] = None 
    words: List[str]

class DictionaryPatch(BaseModel):
    is_active: Optional[bool] = None 
    label: Optional[str] = None