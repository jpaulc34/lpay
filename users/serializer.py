from fastapi import HTTPException, status

from utils.passwords import PasswordHandler
from gateways.database import DatabaseGateway
from users.service import UserService
from utils.logging import create_log

# logging.config.fileConfig('logging.conf', disable_existing_loggers=False)

class User(UserService):
    def __init__(self, db_gateway: DatabaseGateway) -> None:
        self.db_gateway = db_gateway

    def create(self, data):
        password_handler = PasswordHandler()
        data.password = password_handler.hash(data.password)
        create_log("create", data)
        return user_serializer(self.db_gateway.save_document(dict(data)))

    
    def update(self, id, data):
        if hasattr(data, 'created_at'):
            del data.created_at
        create_log("update", dict(data))
        return user_serializer(self.db_gateway.update_document(id, dict(data)))
    
    def delete(self, id):
        result = self.db_gateway.delete_document(id)
        if result:
            create_log("delete", None, None, id)
            return user_serializer(result)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="user not found!")
    
    def filter(self, filter):
        clean_filter = {k: v for k, v in filter.items() if v is not None}
        serialized_users = serialize_list(self.db_gateway.filter_document(clean_filter))
        if serialized_users:
            create_log("filter", None, {'parameters': filter})
            return serialized_users
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="data not found!")

    def get_all(self):
        serialized_users = serialize_list(self.db_gateway.get_collection())
        if serialized_users:
            create_log("get_all")
            return serialized_users
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="users not found!")
    
    def get(self, id):
        result = self.db_gateway.get_document(id)
        if result:
            create_log("get", None, None, id)
            return user_serializer(result)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="user not found!")
    

def user_serializer(data) -> dict:

    user = {
        "id": str(data["_id"]),
        "username": data["username"],
        "email": data["email"],
        "first_name": data["first_name"],
        "last_name": data["last_name"],
        "role": data["role"],
        "status": data["status"],
        "created_at": data["created_at"],
        "updated_at": data["updated_at"]
    }

    if "password" in data:
        user["password"] = data["password"]
    
    return user

def serialize_list(users) -> list:
    return [user_serializer(user) for user in users]