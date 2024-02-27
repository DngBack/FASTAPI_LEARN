# from typing import Annotated 

# from fastapi import FastAPI, Path 
# from pydantic import BaseModel 

# app = FastAPI()

# class Item(BaseModel): 
#     name: str 
#     description: str | None = None 
#     price: float 
#     tax: float | None = None 

# @app.put("/items/{item_id}")
# async def update_item(
#         item_id: Annotated[int, Path(title="The ID of the item to get", ge=0, le =1000)], 
#         q: str | None, 
#         item: Item | None = None, 
# ): 
#     results = {"item_id": item_id}
#     if q: 
#         results.update({"q": q})
#     if item: 
#         results.update({"item": item})
#     return results


# ------------------------------------
#  You can also declare multiple body parameters 
# from fastapi import FastAPI
# from pydantic import BaseModel 

# class Item(BaseModel): 
#     name: str 
#     description: str | None = None 
#     price: float
#     tax: float | None = None 

# class User(BaseModel): 
#     username: str 
#     full_name: str | None = None 

# app = FastAPI()

# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item, user: User):
#     results = {"item_id": item_id, "item": item, "user": user}
#     return results


# -----------------------------------------
# Multiple body params and query 
from typing import Annotated

from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


class User(BaseModel):
    username: str
    full_name: str | None = None


@app.put("/items/{item_id}")
async def update_item(
    *,
    item_id: int,
    item: Item,
    user: User,
    importance: Annotated[int, Body(gt=0)],
    q: str | None = None,
):
    results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
    if q:
        results.update({"q": q})
    return results
