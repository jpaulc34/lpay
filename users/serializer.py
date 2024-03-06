def user_serializer(data) -> dict:

    user = {
        "id": str(data["_id"]),
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

def user_serialize_list(users) -> list:
    return [user_serializer(user) for user in users]