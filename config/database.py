from pymongo import MongoClient
from decouple import config

client = MongoClient(config("db_client"))

db = client.fms

collections = {
    config("tithe_collection"): db[config("tithe_collection")],
    config("user_collection"): db[config("user_collection")],
}

class Database:

    def collection(collection: str):
        if collection in collections:
           print(collections[collection])
           return collections[collection]