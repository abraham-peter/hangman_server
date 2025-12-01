from fastapi import APIRouter,status

router=APIRouter()

@router.post("/sessions",status_code=status.HTTP_201_CREATED)

@router.get("/session/{session_id}",status_code=status.HTTP_201_CREATED)

@router.post("/session/{session_id}/abort",status_code=status.HTTP_200_OK)

@router.get("/session/{session_id}/games",status_code=status.HTTP_201_CREATED)

