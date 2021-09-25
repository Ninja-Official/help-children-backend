from app.database.mongodb import get_database
from motor.motor_asyncio import AsyncIOMotorClient
from fastapi import APIRouter, Body, Depends
from starlette.exceptions import HTTPException
from starlette.status import HTTP_201_CREATED, HTTP_202_ACCEPTED, HTTP_400_BAD_REQUEST
from app.models.event import Event
from app.crud.event import create_event


router = APIRouter()


@router.post(
    "/event/create",
    response_model=Event,
    tags=["event"],
    status_code=HTTP_201_CREATED,
)
async def api_create_event(
        event: Event = Body(...), conn: AsyncIOMotorClient = Depends(get_database)
):
    ...