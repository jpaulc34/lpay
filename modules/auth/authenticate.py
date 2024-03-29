from modules.users.service_implementation import User
from utils.passwords import PasswordHandler
from modules.auth.schema import TokenData
from modules.auth.exception import credentials_exception, user_status_exception
from typing import Annotated

from fastapi import Depends, HTTPException, status, Request
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from datetime import datetime, timedelta
from modules.users.service import UserService
from gateways.database import DatabaseGateway
from decouple import config

SECRET_KEY = config("secret")
ALGORITHM = config("algorithm")
ACCESS_TOKEN_EXPIRE_MINUTES = config("token_expiry")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


class UserAuth:
    @staticmethod
    def authenticate_user(email: str, password: str):
        __user_service: UserService = User(DatabaseGateway(config("user_collection")))
        user = __user_service.filter({"email":email})[0]
        if not user:
            return False
        if not PasswordHandler.verify(password, str(user["password"])):
            return False
        if user["status"] != "active":
            raise user_status_exception
        return user

    @staticmethod
    def create_access_token(data: dict, expires_delta: timedelta = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt
    
    async def check_token(token):
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            user = {
                "email": str(payload.get("sub")),
                "hsh": str(payload.get("hsh")),
                "secret": str(payload.get("secret"))
            }
            if None in user.values() and not PasswordHandler.verify(user["email"], user["hsh"]):
                raise credentials_exception
            return TokenData(**user)
        except JWTError:
            raise credentials_exception
        
    async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
        token_data = await UserAuth.check_token(token)
        __user_service: UserService = User(DatabaseGateway(config("user_collection")))
        user = __user_service.filter({"email":token_data.email})
        if user is None:
            raise credentials_exception
        return user

    async def get_current_active_user(
        current_user: Annotated[User, Depends(get_current_user)]
    ):
        # if current_user.status != "active":
        #     raise HTTPException(status_code=400, detail="User must be activated!")
        return current_user
    
    async def validate_token(token: Annotated[str, Depends(oauth2_scheme)]):
        if await UserAuth.check_token(token):
            return True
        else:
            return False