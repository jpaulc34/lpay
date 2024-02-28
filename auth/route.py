from fastapi import APIRouter, Depends
from users.schema import UserCreate, UserResponse, UserLogin
from users.serializer import User
from auth.authenticate import UserAuth, ACCESS_TOKEN_EXPIRE_MINUTES
from auth.schema import Token
from fastapi import Depends, FastAPI, HTTPException, status
from typing import Any, Annotated
from datetime import timedelta
from utils.passwords import PasswordHandler

auth_router = APIRouter(
        prefix="/auth",
        tags= ["Authentication"],
    )

@auth_router.post("/login", response_model=Token)
async def login_for_access_token(user: UserLogin):
    user = UserAuth.authenticate_user(user.username, user.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=int(ACCESS_TOKEN_EXPIRE_MINUTES))
    access_token = UserAuth.create_access_token(
        data=PasswordHandler.token_data(user), expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

# @auth_router.get("/me/", response_model=UserResponse)
# async def read_users_me(
#     current_user: Annotated[User, Depends(UserAuth.get_current_active_user)]
# ):
#     return current_user

@auth_router.post("/create_account", response_model=UserResponse)
def create_account(user: UserCreate):
    new_user = User(dict(user))
    return new_user.create()