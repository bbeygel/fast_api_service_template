from fastapi import FastAPI

from app.controllers.some import *
from app.models.http import *


def generate_routes(app: FastAPI):
    @app.get("/route")
    async def read_item():
        try:
            res = await get_all()
            return {"data": res}
        except Exception as e:
            return {"error": e}

    @app.get("/route/{item_id}")
    async def read_item(item_id: str):
        try:
            res = await get_something_by_id(item_id)
            return {"data": res, "error": None}
        except Exception as e:
            return {"data": item_id, "error": e}

    @app.post("/route")
    async def create_item(item_details: ItemModel):
        try:
            res = await create_something(item_details)
            return {"data": res, "error": None}
        except Exception as e:
            return {"data": None, "error": e}

    @app.put("/route/{item_id}")
    async def edit_item(item_id: str, item_details: ItemModel):
        try:
            res = await edit_something_by_id(item_id, item_details)
            return {"data": res, "error": None}
        except Exception as e:
            return {"data": None, "error": e}

    @app.delete("/route/{item_id}")
    async def read_item(item_id: str):
        try:
            res = await delete_something_by_id(item_id)
            return {"data": res, "error": None}
        except Exception as e:
            return {"data": None, "error": e}
