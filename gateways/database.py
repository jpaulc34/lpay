from config.database import Database
from bson import ObjectId
from fastapi import HTTPException

class DatabaseGateway:
    def __init__(self, collection_name):
        self.collection_name = collection_name

    def save_document(self, data):
        document = Database.collection(self.collection_name).insert_one(dict(data))
        data["_id"] = str(document.inserted_id)
        return data


    def get_collection(self):
        return Database.collection(self.collection_name).find()
        

    def get_document(self, id:str):    
        vba = ObjectId.is_valid(id)
        if vba:
            return Database.collection(self.collection_name).find_one({"_id": ObjectId(id)})
        
    
    def update_document(self, id, data:dict):
        document = Database.collection(self.collection_name)
        return document.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(data)}, return_document=True)
    

    def delete_document(self, id:str):    
        vba = ObjectId.is_valid(id)
        if vba:
            return Database.collection(self.collection_name).find_one_and_delete({"_id": ObjectId(id)})
        
    def filter_document(self, filter):
        return Database.collection(self.collection_name).find(filter)
