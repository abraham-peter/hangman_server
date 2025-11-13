from fastapi import APIRouter

router=APIRouter()

@router.get("/users/{user_id}/stats")

@router.get("/leaderboard")

@router.get("/stats/global")
