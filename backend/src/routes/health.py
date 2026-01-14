from fastapi import APIRouter,status,Depends,HTTPException
from datetime import datetime,timezone
from sqlalchemy import text
from sqlalchemy.orm import Session
from database import get_db
from config import APP_VERSION
from middleware.rate_limit import RateLimiter

router=APIRouter(
    dependencies=[Depends(RateLimiter(times=10, seconds=60))])

@router.get("/time", status_code=status.HTTP_200_OK)
def server_time():
    now = datetime.now(timezone.utc)
    return {
        "utc": now.isoformat()
    }

@router.get("/healthz")
def health_check(db: Session = Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))
        return {"status": "ok", "database": "ok"}
    except Exception:
        raise HTTPException(status_code=503, detail="database down")
    
@router.get("/version",status_code=status.HTTP_200_OK)
def version():
    return {
        "version": APP_VERSION
    }