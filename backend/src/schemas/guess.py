from pydantic import BaseModel
class GuessRequest(BaseModel):
    letter:str | None
    word:str | None


    
    