from typing import Optional
from pydantic import BaseModel, EmailStr, model_validator, Field, validator, model_validator
from datetime import datetime

class Tithe(BaseModel):
    service: str
    amount: float
    date: str
    created_at: Optional[datetime] = datetime.now()
    updated_at: Optional[datetime] = datetime.now()

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "service": "9am",
                    "amount": 150.0,
                    "date": "2024-03-03"
                }
            ]
        }
    }

class TitheCreateUpdate(Tithe):
    pass

class TitheResponse(BaseModel):
    id: str
    service: str
    amount: float
    date: str
    created_at: Optional[datetime] = datetime.now()
    updated_at: Optional[datetime] = datetime.now()

class TitheFilter(BaseModel):
    service: str = None
    amount: float = None
    start_date: str = None
    end_date: str = None