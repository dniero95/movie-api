import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import pandas as pd
from database import db, movies


# read fake db
db = pd.read_json('db.json')

print(db)


app = FastAPI()

# Handle CORS

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# add hello message


@app.get('/')
def hello():
    return {"message": "Welcome in movie-api"}

# Return all the movies in the database


@app.get('/api/movies')
async def fetch_all_movies():
    all_movies = []
    for movie in movies.find({}, {"_id": 0, "MovieID": 1, "MovieTitle": 1, "MovieGenre": 1}):
        all_movies.append(movie)
    return all_movies

# get a movie by id
# '''The following line of code are commented to test deply


@app.get('/api/movie/{id}')
async def get_movie_by_id(id:int):
    one_movie = []
    for movie in movies.find({"MovieID":id}, {"_id": 0, "MovieID": 1, "MovieTitle": 1, "MovieGenre": 1}):
        one_movie.append(movie)
    return one_movie[0]
   

@app.delete('/api/delete/movie/{id}')
async def delete_movie_by_id(id:int):
    movies.delete_one({"MovieID":id})


# @app.post('/api/add/movie')
#     db.

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=os.getenv(
        "PORT", default=5000), log_level="info")
