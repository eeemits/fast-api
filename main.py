from fastapi import FastAPI

from app.routes.issues import issues as issues_router

app = FastAPI()

app.include_router(issues_router)

# items = [{1: "foo"}, {2: "bar"}, {3: "baz"}]

# @app.get("/health")
# async def health_check():
#     return {"status": "healthy"}

# @app.get("/items/")
# async def read_items():
#     return items

# @app.get("/items/{item_id}")
# def get_item(item_id: int):
#         for item in items:
#             if item_id in item:
#                 return item
#         return {"error": "Item not found"}

# @app.post("/items/")
# def create_item(item: dict):
#     """
#     Creates a new item in the items list.

#     Args:
#         item (dict): dictionary of item to be created

#     Returns:
#         dict: dictionary of item that was created
#     """
#     items.append(item)
#     return item
