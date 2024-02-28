from typing import Optional
from pydantic import BaseModel, EmailStr, model_validator
from datetime import datetime


class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str
    hsh: str
    secret: str