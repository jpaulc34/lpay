from typing import Optional
from pydantic import BaseModel, EmailStr, model_validator, Field, validator, model_validator
from datetime import datetime

# class User(BaseModel):
#     id: str
#     username: str
#     email: EmailStr
#     password: str
#     first_name: str
#     last_name: str
#     role: str
#     status: str
#     created_at: Optional[datetime] = datetime.utcnow()
#     updated_at: Optional[datetime] = datetime.utcnow()
class Timestamp(BaseModel):
    created_at: datetime = datetime.utcnow()
    updated_at: datetime = datetime.utcnow()

class UserCreate(Timestamp):
    email: EmailStr
    password: str
    first_name: str
    last_name: str
    role: str
    status: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "email": "user_string@yahoo.com.ph",
                    "password": "password123",
                    "first_name": "Juan",
                    "last_name": "Dela Cruz",
                    "role": "treasurer",
                    "status": "pending",
                }
            ]
        }
    }


class UserUpdate(Timestamp):
    email: EmailStr
    first_name: str
    last_name: str
    role: str
    status: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "email": "user_string@yahoo.com.ph",
                    "password": "password123",
                    "first_name": "Juan",
                    "last_name": "Dela Cruz",
                    "role": "treasurer",
                    "status": "pending",
                }
            ]
        }
    }

class UserResponse(BaseModel):
    id: str
    email: EmailStr
    first_name: str
    last_name: str
    role: str
    status: str
    created_at: Optional[datetime] = datetime.utcnow()
    updated_at: Optional[datetime] = datetime.utcnow()

class UserLogin(BaseModel):
    email: str
    password: str

class UserFilter(BaseModel):
    email: Optional[EmailStr] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    role: Optional[str] = None
    status: Optional[str] = None