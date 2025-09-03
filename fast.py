from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()
items = []


class Item(BaseModel):
    name: str


@app.get("/")
def root():
    return {"message": "Hello, Worrld!"}


@app.post("/items/")
def new_item(new_items: List[Item]):
    for item in new_items:
        items.append(item.name)
    return items

@app.get("/items/")
def list_items(limit: int = 4):
    return items[0:limit]

@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id < 0 or item_id >= len(items):
        return {"error": "Item not found"}, 404
    item = items[item_id]
    return {"item": item}
