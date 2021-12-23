from typing import Mapping
from fastapi import FastAPI

from model import get_news


app = FastAPI()

@app.get('/home={count}')
async def dictionary(count: int):
    news_arr = get_news(count)
    return news_arr

@app.get("/")
async def root():
    return {"message": "Hello World"}


