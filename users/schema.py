from typing import Optional
from pydantic import BaseModel, EmailStr, model_validator, Field
from datetime import datetime

class User(BaseModel):
    id: str
    username: str
    email: EmailStr
    password: str
    first_name: str
    last_name: str
    role: str
    status: str
    created_at: Optional[datetime] = datetime.now()
    updated_at: Optional[datetime] = datetime.now()

class UserCreateUpdate(User):
    class Config:
        exclude: {"id"}
        orm_mode: True

class UserResponse(User):
    class Config:
        exclude: {"password"}

class UserLogin(BaseModel):
    email: str
    password: str

class UserFilter(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    role: Optional[str] = None
    status: Optional[str] = None