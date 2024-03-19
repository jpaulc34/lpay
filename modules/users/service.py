from abc import ABC
from ...modules.users.schema import UserResponse

class UserService(ABC):
    
    def create(self) -> UserResponse:
        raise NotImplementedError()

    def update(self, id : str) -> UserResponse:
        raise NotImplementedError()

    def delete(self, id : str) -> UserResponse:
        raise NotImplementedError()

    def filter(self, filter : dict) -> list[UserResponse]:
        raise NotImplementedError()

    def get_all() -> list[UserResponse]:
        raise NotImplementedError()

    def get(self, id : str) -> UserResponse:
        raise NotImplementedError()