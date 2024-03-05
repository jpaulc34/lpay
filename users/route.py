from fastapi import APIRouter, Depends
from users.serializer import User
from users.schema import UserResponse, UserCreateUpdate, UserFilter
from users.service import UserService
from gateways.database import DatabaseGateway
from decouple import config

user_router = APIRouter(
        prefix="/users",
        tags= ["Users"],
        # dependencies= [Depends(UserAuth.validate_token)]
    )


__user_service: UserService = User(DatabaseGateway(config("user_collection")))

@user_router.get("/",response_model=list[UserResponse])
def get_users():
    return __user_service.get_all()

@user_router.get("/filter", response_model=list[UserResponse])
def filter_user(query: UserFilter = Depends()):
    return __user_service.filter(dict(query))

@user_router.get("/{id}", response_model=UserResponse)
def get_user(id: str):
    return __user_service.get(id)

@user_router.post("/", response_model=UserResponse)
def save_user(user: UserCreateUpdate):
    return __user_service.create(user)

@user_router.put("/{id}", response_model=UserResponse)
def update_user(id: str, updated_user: UserCreateUpdate):
    return __user_service.update(id, updated_user)

@user_router.delete("/{id}")
def delete_user(id: str):
    return __user_service.delete(id)