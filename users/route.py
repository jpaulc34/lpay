from fastapi import APIRouter, Depends
from users.serializer import User
from users.schema import UserResponse, UserCreateUpdate, UserFilter
from users.service import UserService
from auth.authenticate import UserAuth
from gateways.database import DatabaseGateway


user_router = APIRouter(
        prefix="/users",
        tags= ["Users"],
        # dependencies= [Depends(UserAuth.validate_token)]
    )

__user_service: UserService = User

@user_router.get("/",response_model=list[UserResponse])
def get_users():
    return __user_service(DatabaseGateway).get_all()

@user_router.get("/filter", response_model=list[UserResponse])
def filter_user(query: UserFilter = Depends()):
    filter = __user_service(DatabaseGateway).filter(dict(query))
    return filter

@user_router.get("/{id}", response_model=UserResponse)
def get_user(id: str):
    user = __user_service(DatabaseGateway).get(id)
    return user

@user_router.post("/", response_model=UserResponse)
def save_user(user: UserCreateUpdate):
    return __user_service(DatabaseGateway, dict(user)).create()

@user_router.put("/{id}", response_model=UserResponse)
def update_user(id: str, updated_user: UserCreateUpdate):
    return __user_service(DatabaseGateway, updated_user).update(id)

@user_router.delete("/{id}")
def delete_user(id: str):
    user = __user_service(DatabaseGateway).delete(id)
    return user