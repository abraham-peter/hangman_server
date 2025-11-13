from fastapi import APIRouter

router=APIRouter()

@router.get("/admin/dictionaries")

@router.post("/admin/dictionaries")

@router.patch("/admin/dictionaries/{id}")

@router.get("/admin/dictionaries/{id}/words")