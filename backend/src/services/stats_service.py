from models import GameStatus

def session_stats(games:list[dict]):
    finished=0
    wins=0
    losses=0
    total_guesses=0
    total_wrong=0
    for g in games:
        status=g["status"]
        if status == GameStatus.WON or status== GameStatus.LOST:
            finished+=1
            total_guesses+=g["total_guesses"]
            total_wrong+=len(g["wrong_letters"])
            if status==GameStatus.WON:
                wins+=1
            else:
                losses+=1
    win_rate=0
    avg_guesses=0
    avg_wrong=0
    if finished>0:
        win_rate=wins/finished
        avg_guesses=total_guesses/finished
        avg_wrong=total_wrong/finished

    return{
        "games_total":len(games),
        "games_finished":finished,
        "wins":wins,
        "losses":losses,
        "win_rate":win_rate,
        "avg_total_guesses":avg_guesses,
        "avg_wrong_letters":avg_wrong,
    } 