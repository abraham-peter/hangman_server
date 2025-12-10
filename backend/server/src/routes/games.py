from fastapi import APIRouter

router=APIRouter()
@app.get("/games/")
def read_games(db: Session= Depends(get_db)):
    games=db.query(Game).all()
    return games

@router.post("/session/{session_id}/games")

@router.get("/sessions/{session_id}/games/{game_id}/state")

@router.post("/sessions/{session_id}/games/{game_id}/guess")

@router.get("/sessions/{session_id}/games/{game_id}/history")

@router.post("/sessions/{session_id}/games/{game_id}/abort")
