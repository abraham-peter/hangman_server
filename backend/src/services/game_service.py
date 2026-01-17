
from fastapi import HTTPException, status
from models import Game 
from sqlalchemy.orm import Session 
from models import Session as SessionModel
from datetime import datetime,timezone
from schemas.game import GameStatus 
from schemas.session import SessionStatus
import uuid
from uuid import UUID

def get_owned_game(db: Session, game_id: str, user_id: int) -> Game:
#    """  
#    Returneaza jocul daca apartine user-ului.
#    Arunca HTTPException(404) daca nu exista / nu e al user-ului.
#    """
    game_uuid=UUID(game_id)
    game = ( 
        db.query(Game)
        .join(SessionModel, Game.session_id==SessionModel.session_id)
        .filter(Game.game_id==game_uuid)
        .filter(SessionModel.user_id==user_id)
        .first()
    )
    if not game:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Game not found or not owned by user"
        )
    return game

def apply_guess(game:Game,guess:str):
#    #Terminare program
#    if game.status !="IN_PROGRESS":
#        return game

#    """
#    Aplică o ghicire pentru o literă la jocul curent.  
#    Modifică game direct (ORM). Commit-ul se face în route.
#    Ridică ValueError dacă litera este invalidă sau deja ghicită.
#    """

    letter=guess.lower()
    # Validare Litera 
    if len(letter) != 1 or not letter.isalpha():
        raise ValueError("Provide only one alphabet letter.")
    # Verificam daca litera a fost, sau nu, ghicita deja.
    if letter in game.guessed_letters or letter in game.wrong_letters:
        raise ValueError(f"Letter '{letter}' has already been guessed.")
    # Ghicire corecta
    if letter in game.word.lower():
        game.guessed_letters.append(letter)
    else:
        #Ghicire gresita
        game.wrong_letters.append(letter)
        game.remaining_misses -= 1
    # Updatam pattern-ul
    new_pattern=""
    for char in game.word:
        if char.lower() in game.guessed_letters:
            new_pattern+=char
        else:
            new_pattern+="*"
    game.pattern=new_pattern
    #Se intelege (Asta a zis Peter)
    if "*" not in new_pattern:
        game.status=GameStatus.WON
        game.finished_at=datetime.now(timezone.utc)
    elif game.remaining_misses<=0:
        game.status=GameStatus.LOST
        game.finished_at=datetime.now(timezone.utc) 
    return game  





