from fastapi import APIRouter,status
from schemas.game import PostResponse
router=APIRouter()


@router.post("/session/{session_id}/games",response_model=PostResponse,status_code=status.HTTP_201_CREATED)

@router.get("/sessions/{session_id}/games/{game_id}/state",status_code=status.HTTP_200_OK)

@router.post("/sessions/{session_id}/games/{game_id}/guess",status_code=status.HTTP_200_OK)

@router.get("/sessions/{session_id}/games/{game_id}/history",status_code=status.HTTP_201_CREATED)

@router.post("/sessions/{session_id}/games/{game_id}/abort",status_code=status.HTTP_200_OK)
def a():
    pass