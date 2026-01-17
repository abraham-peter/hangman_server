from fastapi import APIRouter,status, HTTPException, status
from models import UserDB 

def admin_required(user: UserDB):
    if not user.is_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN
            detail="Asta este Admin Panel :("
        )

router=APIRouter(prefix="/admin/dictionaries",tags=["Admin Dictionaries"])

