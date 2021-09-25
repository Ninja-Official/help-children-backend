from app.core.events import on_start_application, on_stop_application
from fastapi import FastAPI
from .core.config import PROJECT_NAME, API_V1_PREFIX
from .api.api_v1.routes import router as api_router
from .core.events import on_start_application, on_stop_application

app = FastAPI(title=PROJECT_NAME)


app.add_event_handler("startup", on_start_application)
app.add_event_handler("shutdown", on_stop_application)

app.include_router(api_router, prefix=API_V1_PREFIX)
