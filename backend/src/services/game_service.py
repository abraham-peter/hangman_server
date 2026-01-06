from schemas.session import GuessRequest
from datetime import datetime,timezone
def apply_guess(game:dict,guess:GuessRequest)->dict[str,str]:
    #Terminare program
    if game["status"] !="IN_PROGRESS":
        raise ValueError("Game already finished")
    if not guess.letter:
        raise ValueError("Guess Required")

    #Incercarea literei si plasarea ei
    word=game["word"]
    if guess.letter:
        letter=guess.letter.lower()
        if letter in game["guessed_letters"] or letter in game["wrong_letters"]:
            raise ValueError("Letter already guessed")
        if len(letter)>1 and letter.isalpha():
            raise ValueError("Provide only one letter and not symbols")
        if letter in word:
            game["guessed_letters"].add(letter)
        else:
            game["wrong_letters"].add(letter)
            game["remaining_misses"]-=1
    #incercare directa a cuvantului(daca e cazul)
    #update la pattern
    new_pattern=""
    for char in word:
        if char in game["guessed_letters"]:
            new_pattern+=char
        else:
            new_pattern+="*"
    game["pattern"]=new_pattern
    #Se intelege
    if game["pattern"]==word:   
        game["status"]="WON"
    elif game["remaining_misses"]<=0:
        game["status"]="LOST" 
    return game  
def record_history(game:dict):
    snapshot={
        "timestamp":datetime.now(timezone.utc).isoformat(),
        "pattern":game["pattern"],
        "remaining_misses":list(game["remaining_misses"]),
        "guessed_letters":list(game["guessed_letters"]),
        "status":game["status"],
    } 
    game["hystory"].append(snapshot)
def abort_game(game:dict):
    if game["status"]!="IN_PROGRESS":
        raise ValueError("Game is not in progress")
    game["status"]="ABORTED"
    game["aborted_at"]=datetime.now(timezone.utc).isoformat()
def playable_in_guess(game:dict):
    if game["status"]!="IN_PROGRESS":
        raise ValueError("Game is not in progress")



