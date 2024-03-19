from pymongo import MongoClient
from decouple import config
from ..utils.logging import database_error

client = MongoClient(config("db_client"))

db = client.fms

collections = {
    config("tithe_collection"): db[config("tithe_collection")],
    config("user_collection"): db[config("user_collection")],
}

class Database:

    def collection(collection: str):
        try:
            if collection in collections:
                return collections[collection]
        except Exception as e:
            database_error(e)