from fastapi import APIRouter,status
from fastapi.responses import JSONResponse
from schemas.game import PostResponse,PostCreate
router=APIRouter()

cuvant="MERE"
status_game=["NOT_STARTED","IN_PROGRESS","WON","LOST"]
just_for_test= {
  "game_id": "g_456",
  "session_id": "s_789",
  "status": f"{status_game[0]}",
  "length": 7,
  "pattern": "*******",
  "guessed_letters": [],
  "wrong_letters": [],
  "remaining_misses": 6,
  "total_guesses": 0,
  "result": None }

@router.post("/session/{session_id}/games",response_model=PostResponse,status_code=status.HTTP_201_CREATED)
async def game_test(PostCreate:PostCreate):
    return JSONResponse(status_code=status.HTTP_201_CREATED,content=just_for_test)  
    
    
@router.get("/sessions/{session_id}/games/{game_id}/state",status_code=status.HTTP_200_OK)

@router.post("/sessions/{session_id}/games/{game_id}/guess",status_code=status.HTTP_200_OK)

@router.get("/sessions/{session_id}/games/{game_id}/history",status_code=status.HTTP_201_CREATED)

@router.post("/sessions/{session_id}/games/{game_id}/abort",status_code=status.HTTP_200_OK)