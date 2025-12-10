from fastapi import APIRouter,status
from schemas.session import PostCreate,PostResponse
router=APIRouter()

@router.post("/sessions",status_code=status.HTTP_201_CREATED)
async def creaza_sesiune_joc(date:PostCreate)->PostResponse:
    return PostResponse(
        session_id="s_789",
        num_games=date.num_games
    )

@router.get("/session/{session_id}",status_code=status.HTTP_201_CREATED)

@router.post("/session/{session_id}/abort",status_code=status.HTTP_200_OK)

@router.get("/session/{session_id}/games",status_code=status.HTTP_201_CREATED)

