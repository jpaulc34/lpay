from fastapi import APIRouter, Depends
from users.schema import UserResponse, UserLogin, UserCreate
from users.service_implementation import User
from users.service import UserService
from gateways.database import DatabaseGateway
from auth.authenticate import UserAuth, ACCESS_TOKEN_EXPIRE_MINUTES
from auth.schema import Token
from fastapi import Depends, HTTPException, status
from typing import Any, Annotated
from datetime import timedelta
from utils.passwords import PasswordHandler
from decouple import config

router = APIRouter(
        prefix="/auth",
        tags= ["Authentication"],
    )

@router.post("/login", response_model=Token)
async def login_for_access_token(user: UserLogin):
    user = UserAuth.authenticate_user(user.email, user.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=int(ACCESS_TOKEN_EXPIRE_MINUTES))
    access_token = UserAuth.create_access_token(
        data=PasswordHandler.token_data(user), expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

# @router.get("/me/", response_model=UserResponse)
# async def read_users_me(
#     current_user: Annotated[User, Depends(UserAuth.get_current_active_user)]
# ):
#     return current_user

@router.post("/create_account", response_model=UserResponse)
def create_account(user: UserCreate):
    __user_service: UserService = User(DatabaseGateway(config("user_collection")))
    return __user_service.create(user)