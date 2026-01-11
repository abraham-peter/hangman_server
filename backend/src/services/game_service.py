from schemas.session import GuessRequest
from datetime import datetime,timezone
def apply_guess(game,guess:GuessRequest):
    #Terminare program
    if game.status !="IN_PROGRESS":
        return game

    #Incercarea literei si plasarea ei
    word=game.word.lower()
    if guess.letter:
        letter=guess.letter.lower()
        if letter in game.guessed_letters or letter in game.wrong_letters:
            raise ValueError("Letter already guessed")
        if len(letter)!=1 and letter.isalpha():
            raise ValueError("Provide only one letter and not symbols")
        if letter in word:
            game.guessed_letters.add(letter)
        else:
            game.wrong_letters.add(letter)
            game.remaining_misses-=1
    #incercare directa a cuvantului(daca e cazul)
    #update la pattern
    new_pattern=""
    for char in word:
        if char in game.guessed_letters:
            new_pattern+=char
        else:
            new_pattern+="*"
    game.pattern=new_pattern
    #Se intelege
    if game.pattern==word:   
        game.status="WON"
    elif game.remaining_misses<=0:
        game.status="LOST" 
    return game  





