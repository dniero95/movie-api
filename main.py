import os
from fastapi import FastAPI
import uvicorn
import pandas as pd

db = pd.read_json('db.json')

print(db)

app = FastAPI()



# Return all the movies in the database
@app.get('/api/movies')
async def fetch_all_movies():
    return db.to_dict('index')

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=os.getenv("PORT", default=5000), log_level="info")