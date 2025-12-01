from fastapi import APIRouter,status

router=APIRouter()

@router.get("/users/{user_id}/stats",status_code=status.HTTP_201_CREATED)

@router.get("/leaderboard",status_code=status.HTTP_201_CREATED)

@router.get("/stats/global",status_code=status.HTTP_201_CREATED)
