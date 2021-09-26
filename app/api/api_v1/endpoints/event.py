import json

from typing import List
from app.database.mongodb import get_database
from motor.motor_asyncio import AsyncIOMotorClient
from fastapi import APIRouter, Body, Depends, File, UploadFile, Form
from starlette.exceptions import HTTPException
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_202_ACCEPTED, HTTP_400_BAD_REQUEST
from app.models.event import Event
from app.crud.event import create_event, get_event_by_id, get_events
from types import SimpleNamespace

router = APIRouter()
    
@router.post(
    "/events/create",
    tags=["event"],
    status_code=HTTP_201_CREATED,
)
async def api_create_event(
        event: str = Form(...), userpic: UploadFile = File(...), conn: AsyncIOMotorClient = Depends(get_database)
):
    print(userpic.filename)
    event_dict = json.loads(event)
    event = Event(**event_dict)

    async with await conn.start_session() as s:
        async with s.start_transaction():
            await create_event(conn, event, image=userpic)

    # {   "name": "string",   "consumers": "string",   "resources": "string",   "description": "string",   "location": "string",   "date": "string" }

@router.get(
    "/events",
    response_model=List[Event],
    tags=["event"],
    status_code=HTTP_200_OK,
)
async def api_getch_events(
        events_ammount: int = Body(...), event_id: int = Body(...), conn: AsyncIOMotorClient = Depends(get_database)
):
    async with await conn.start_session() as s:
        async with s.start_transaction():
            return await get_events(conn, event_id, events_ammount)

@router.get(
    "/events/{event_id}",
    response_model=Event,
    tags=["event"],
    status_code=HTTP_200_OK,
)
async def api_getch_event(
        event_id: str, conn: AsyncIOMotorClient = Depends(get_database)
):
    async with await conn.start_session() as s:
        async with s.start_transaction():
            return await get_event_by_id(conn, event_id)

