from utils.passwords import PasswordHandler
from gateways.database import DatabaseGateway
from fastapi import HTTPException, status

collection_name = "users"

class User:
    def __init__(self, data) -> None:
        self.data = data

    def create(self):
        password_handler = PasswordHandler()
        self.data["password"] = password_handler.hash(self.data["password"])
        user = DatabaseGateway(collection_name)
        return user_serializer(user.save_document(self.data))
    
    def update(self, id):
        del self.data.created_at
        user = DatabaseGateway(collection_name)
        return user_serializer(user.update_document(id, self.data))
    
    def delete(id):
        user = DatabaseGateway(collection_name)
        result = user.delete_document(id)
        if result:
            return user_serializer(result)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="user not found!")
    
    def filter(filter):
        clean_filter = {k: v for k, v in filter.items() if v is not None}

        users = DatabaseGateway(collection_name)
        filtered_document = users.filter_document(clean_filter)
        serialized_users = serialize_list(filtered_document)
        if serialized_users:
            return serialized_users
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="user not found!")

    def get_all():
        users = DatabaseGateway(collection_name)
        serialized_users = serialize_list(users.get_collection())
        if serialized_users:
            return serialized_users
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="users not found!")
    
    def get(id):
        user = DatabaseGateway(collection_name)
        result = user.get_document(id)
        if result:
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
    return user

def serialize_list(users) -> list:
    return [user_serializer(user) for user in users]