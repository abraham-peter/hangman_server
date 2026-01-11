from fastapi import APIRouter,status

router=APIRouter()

@router.get("/healthz",status_code=status.HTTP_201_CREATED)

@router.get("/version",status_code=status.HTTP_200_OK)

@router.get("/time",status_code=status.HTTP_200_OK)

