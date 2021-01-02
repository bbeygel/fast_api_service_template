from fastapi import FastAPI
import app.routers as routers

app = FastAPI()

routers.setup_routers(app)
