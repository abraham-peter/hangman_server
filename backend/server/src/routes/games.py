from fastapi import APIRouter

router=APIRouter()


@router.post("/session/{session_id}/games")

@router.get("/sessions/{session_id}/games/{game_id}/state")

@router.post("/sessions/{session_id}/games/{game_id}/guess")

@router.get("/sessions/{session_id}/games/{game_id}/history")

@router.post("/sessions/{session_id}/games/{game_id}/abort")
