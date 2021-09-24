from fastapi import FastAPI
from .core.config import PROJECT_NAME, API_V1_PREFIX
from .api.api_v1.routes import router as api_router
from .database.mongodb_connection import connect_to_mongo, close_mongo_connection

app = FastAPI(title=PROJECT_NAME)


app.add_event_handler("startup", connect_to_mongo)
app.add_event_handler("shutdown", close_mongo_connection)

app.include_router(api_router, prefix=API_V1_PREFIX)
