import os
import pymongo
from dotenv import load_dotenv

load_dotenv()
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_USER = os.getenv('DB_USER')
mongo_client = pymongo.MongoClient(f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@movies-api.mnn4cyp.mongodb.net/?retryWrites=true&w=majority")
db = mongo_client["movies-api-db"]

movies = db["movies"]

# code from:
# https://www.geeksforgeeks.org/read-json-file-using-python/

'''Comment this code since the movies are already in the db

with open('./db.json') as file:
    movies_list = json.load(file)
    

x = movies_collection.insert_many(movies_list)
'''


# all_movies = []
# for movie in movies.find({},{ "_id": 0,"MovieID":1, "MovieTitle": 1, "MovieGenre": 1 }):
#   all_movies.append(movie)

