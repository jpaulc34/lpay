from fastapi import APIRouter, Depends
from users.service_implementation import User
from users.schema import UserResponse, UserFilter, UserCreate, UserUpdate
from users.service import UserService
from gateways.database import DatabaseGateway
from decouple import config

router = APIRouter(
        prefix="/users",
        tags= ["Users"],
        # dependencies= [Depends(UserAuth.validate_token)]
    )


__user_service: UserService = User(DatabaseGateway(config("user_collection")))

@router.get("/",response_model=list[UserResponse])
def get_users():
    return __user_service.get_all()

@router.get("/filter", response_model=list[UserResponse])
def filter_user(query: UserFilter = Depends()):
    return __user_service.filter(dict(query))

@router.get("/{id}", response_model=UserResponse)
def get_user(id: str):
    return __user_service.get(id)

@router.post("/", response_model=UserResponse)
def save_user(user: UserCreate):
    return __user_service.create(user)

@router.put("/{id}", response_model=UserResponse)
def update_user(id: str, updated_user: UserUpdate):
    return __user_service.update(id, updated_user)

@router.delete("/{id}")
def delete_user(id: str):
    return __user_service.delete(id)