from fastapi import APIRouter,status

router=APIRouter()

@router.get("/admin/dictionaries",status_code=status.HTTP_200_OK)

@router.post("/admin/dictionaries",status_code=status.HTTP_201_CREATED)

@router.patch("/admin/dictionaries/{id}",status_code=status.HTTP_200_OK)

@router.get("/admin/dictionaries/{id}/words",status_code=status.HTTP_200_OK)