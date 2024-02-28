from pymongo import MongoClient
from decouple import config

client = MongoClient(config("db_client"))

db = client.fms

collections = {
    "tithes" : db['tithes'],
    "users": db['users']
}

class Database:

    def collection(collection: str):
        if collection in collections:
           return collections[collection]