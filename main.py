import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import pandas as pd


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
    return db.to_dict('index')

# get a movie by id

@app.get('/api/movie/{id}')
async def get_movie_by_id(id:int):
    return db.query('MovieID == @id').to_dict('index')

@app.delete('/api/delete/movie/{id}')
async def delete_movie_by_id(id:int):
    db.drop(db[db.MovieID == id].index, inplace=True)
    
# @app.post('/api/add/movie')
#     db.

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=os.getenv("PORT", default=5000), log_level="info")