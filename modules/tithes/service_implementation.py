from fastapi import HTTPException, status

from ...gateways.database import DatabaseGateway
from ...modules.tithes.service import TitheService
from ...utils.logging import create_log_operation
from ...utils.timestamps import set_timestamps, set_updated_at
from ...modules.tithes.serializer import tithe_serializer, tithe_serialize_list
from datetime import datetime

# logging.config.fileConfig('logging.conf', disable_existing_loggers=False)

class Tithe(TitheService):
    def __init__(self, db_gateway: DatabaseGateway) -> None:
        self.db_gateway = db_gateway

    def create(self, data):
        set_timestamps(data)
        create_log_operation("create", data)
        return tithe_serializer(self.db_gateway.save_document(dict(data)))

    
    def update(self, id, data):
        set_updated_at(data)
        create_log_operation("update", dict(data), None, id)
        return tithe_serializer(self.db_gateway.update_document(id, dict(data)))
    
    def delete(self, id):
        result = self.db_gateway.delete_document(id)
        if result:
            create_log_operation("delete", None, None, id)
            return tithe_serializer(result)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="data not found!")
    
    def filter(self, filter):
        clean_filter = {k: v for k, v in filter.items() if v is not None}
        serialized_users = tithe_serialize_list(self.db_gateway.filter_document(clean_filter))
        if serialized_users:
            create_log_operation("filter", None, {'parameters': filter})
            return serialized_users
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="data not found!")

    def get_all(self):
        serialized_users = tithe_serialize_list(self.db_gateway.get_collection())
        if serialized_users:
            create_log_operation("get_all")
            return serialized_users
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="data not found!")
    
    def get(self, id):
        result = self.db_gateway.get_document(id)
        if result:
            create_log_operation("get", None, None, id)
            return tithe_serializer(result)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="data not found!")