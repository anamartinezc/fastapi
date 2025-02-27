from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import requests

app = FastAPI()

class Post(BaseModel):
    userId: int
    id: int
    title: str
    body: str

@app.get("/posts", response_model=List[Post])
async def get_posts():
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/posts")
        if response.status_code == 200:
            return response.json()
        raise HTTPException(status_code=response.status_code, detail="Error fetching posts")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/posts/{post_id}", response_model=Post)
async def get_post(post_id: int):
    try:
        response = requests.get(f"https://jsonplaceholder.typicode.com/posts/{post_id}")
        if response.status_code == 200:
            return response.json()
        raise HTTPException(status_code=404, detail="Post not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/posts", response_model=Post)
async def create_post(post: Post):
    try:
        response = requests.post(
            "https://jsonplaceholder.typicode.com/posts",
            json=post.dict()
        )
        if response.status_code == 201:
            return response.json()
        raise HTTPException(status_code=response.status_code, detail="Error creating post")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    print(HOLA JENNI)