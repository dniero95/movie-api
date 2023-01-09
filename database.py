import pymongo
import json



mongo_client = pymongo.MongoClient("mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+1.5.4")
db = mongo_client["movies-api-db"]

movies_collection = db["movies"]

# code from:
# https://www.geeksforgeeks.org/read-json-file-using-python/

'''Comment this code since the movies are already in the db

with open('./db.json') as file:
    movies_list = json.load(file)
    

x = movies_collection.insert_many(movies_list)
'''



for x in movies_collection.find({},{ "_id": 0,"MovieID":1, "MovieTitle": 1, "MovieGenre": 1 }):
  print(x)

