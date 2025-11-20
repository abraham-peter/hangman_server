from fastapi import APIRouter,status
from schemas.user import PostCreate
router=APIRouter()

@router.post("/auth/register",status_code=status.HTTP_200_OK)

@router.post("/auth/login",status_code=status.HTTP_201_CREATED)

@router.post("/auth/refresh",status_code=status.HTTP_200_OK)

@router.get("/users/me",response_model=PostCreate,status_code=status.HTTP_201_CREATED)

