import os

from fastapi import FastAPI


def generate_routes(app: FastAPI):
    @app.get("/")
    async def _():
        service_name = os.getenv("SERVICE_NAME", "RANDOM SERVICE")
        return {"service_name": service_name}
