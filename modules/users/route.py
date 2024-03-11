from fastapi import APIRouter, Depends
from modules.users.service_implementation import User
from modules.users.schema import UserResponse, UserFilter, UserCreate, UserUpdate, UserListResponse
from modules.users.service import UserService
from modules.auth.authenticate import UserAuth
from gateways.database import DatabaseGateway
from decouple import config

router = APIRouter(
        prefix="/users",
        tags= ["Users"],
        dependencies= [Depends(UserAuth.validate_token)]
    )


__user_service: UserService = User(DatabaseGateway(config("user_collection")))

@router.get("/",response_model=list[UserListResponse])
def get_users():
    return __user_service.get_all()

@router.get("/filter", response_model=list[UserListResponse])
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

@router.delete("/{id}",response_model=UserResponse)
def delete_user(id: str):
    return __user_service.delete(id)