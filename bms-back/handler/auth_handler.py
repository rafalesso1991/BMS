from fastapi import HTTPException

# HTTP EXCEPTION "INVALID AUTHENTICATION CREDENTIALS"
def invalid_credentials():
    raise HTTPException(
        status_code=401,
        detail="Invalid Authentication Credentials",
        headers={"WWW-Authenticate": "Bearer"}
    )
# HTTP EXCEPTION "TOKEN EXPIRED"
def token_expired():
    raise HTTPException (
        status_code=440,
        detail='Session Expired'
    )
