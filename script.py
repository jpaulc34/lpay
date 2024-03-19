from pymongo import MongoClient
from decouple import config

client = MongoClient(config("db_client"))
db = client.fms

users = db[config("user_collection")].find()
for i in users:
    print(i)