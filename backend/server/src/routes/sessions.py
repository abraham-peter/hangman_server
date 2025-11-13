from fastapi import APIRouter

router=APIRouter()

@router.post("/sessions")

@router.get("/session/{session_id}")

@router.post("/session/{session_id}/abort")

@router.get("/session/{session_id}/games")

