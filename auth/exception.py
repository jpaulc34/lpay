from fastapi import HTTPException, status

credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

user_status_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Account is on pending status! Please contact the administrator.",
        headers={"WWW-Authenticate": "Bearer"},
    )