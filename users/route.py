from fastapi import APIRouter, Depends
from users.serializer import User
from users.schema import UserUpdate, UserResponse, UserCreate, UserFilter


user_router = APIRouter(
        prefix="/users",
        tags= ["Users"]
    )


@user_router.get("/",response_model=list[UserResponse])
def get_users():
    return User.get_all()

@user_router.get("/filter", response_model=list[UserResponse])
def filter_user(query: UserFilter = Depends()):
    filter = User.filter(dict(query))
    return filter

@user_router.get("/{id}", response_model=UserResponse)
def get_user(id: str):
    user = User.get(id)
    return user

@user_router.post("/", response_model=UserResponse)
def save_user(user: UserCreate):
    new_user = User(dict(user))
    return new_user.create()

@user_router.put("/{id}", response_model=UserResponse)
def update_user(id: str, updated_user: UserUpdate):
    user = User(updated_user)
    return user.update(id)

@user_router.delete("/{id}")
def delete_user(id: str):
    user = User.delete(id)
    return user