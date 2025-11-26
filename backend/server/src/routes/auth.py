from fastapi import APIRouter,status,Form
from schemas.user import PostCreate
from typing import Annotated
from schemas.auth import FormData

router=APIRouter()

@router.post("/auth/register",status_code=status.HTTP_200_OK)

@router.post("/auth/login",status_code=status.HTTP_201_CREATED)
async def login(data:Annotated[FormData,Form()]):
    return data

@router.post("/auth/refresh",status_code=status.HTTP_200_OK)

@router.get("/users/me",response_model=PostCreate,status_code=status.HTTP_201_CREATED)
def nothing():
    pass