from pymongo import MongoClient
from decouple import config

client = MongoClient(config("db_client"))

db = client.fms

collections = {
    config("tithe_collection"): config("tithe_collection"),
    config("user_collection"): config("user_collection")
}

class Database:

    def collection(collection: str):
        if collection in collections:
           return collections[collection]