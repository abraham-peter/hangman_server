from fastapi import APIRouter,status, Depends
from middleware.rate_limit import RateLimiter


router=APIRouter(
    dependencies=[Depends(RateLimiter(times=10, seconds=60))])

@router.get("/users/{user_id}/stats",status_code=status.HTTP_201_CREATED)

@router.get("/leaderboard",status_code=status.HTTP_201_CREATED)

@router.get("/stats/global",status_code=status.HTTP_201_CREATED)
