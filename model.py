from pydantic import BaseModel
from typing import List

class Movie(BaseModel):
    MovieID:int
    MovieTitle:str
    MovieGenre:List[str]