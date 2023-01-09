import pymongo
import json



mongo_client = pymongo.MongoClient("mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+1.5.4")
db = mongo_client["movies-api-db"]

movies_collection = db["movies"]

# code from:
# https://www.geeksforgeeks.org/read-json-file-using-python/
with open('./db.json') as file:
    movies_list = json.load(file)
    

x = movies_collection.insert_many(movies_list)