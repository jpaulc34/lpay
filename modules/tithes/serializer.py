def tithe_serializer(data) -> dict:

    tithe = {
        "id": str(data["_id"]),
        "service": data["service"],
        "amount": data["amount"],
        "date": data["date"],
        "created_at": data["created_at"],
        "updated_at": data["updated_at"]
    }
    
    return tithe

def tithe_serialize_list(tithes) -> list:
    return [tithe_serializer(tithe) for tithe in tithes]