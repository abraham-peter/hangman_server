from fastapi import Request
from fastapi_limiter.depends import RateLimiter
from fastapi.security.utils import get_authorization_scheme_param
import jwt
from dotenv import load_dotenv
import os
load_dotenv()
SECRET_KEY=os.getenv("SECRET_KEY")
ALGORITHM=os.getenv("ALGORITHM")
async def rate_limit_key(request:Request)->str | None:
    token=request.cookies.get("access_token")

    if token:
        scheme,param=get_authorization_scheme_param(token)
        if scheme.lower()=="bearer":
            try:
                payload=jwt.decode(param,SECRET_KEY,algorithms=[ALGORITHM],options={"verify_exp":False})
                user_id=payload.get("sub")
                if user_id:
                    return f"user id:{user_id}"
            except jwt.PyJWTError:
                pass
    client_ip=request.client.host if request.client else "unknown"
    return f"ip:{client_ip}"

def rate_limit(times: int, seconds: int):
    return RateLimiter(
        times=times,
        seconds=seconds,
        identifier=rate_limit_key,
    )

