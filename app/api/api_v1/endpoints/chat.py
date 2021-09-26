from fastapi import APIRouter, Body, Depends
from starlette.status import HTTP_201_CREATED

from ....crud.chat import add_message, add_user_to_chat, create_chat_room
from ....database.mongodb import AsyncIOMotorClient, get_database
from ....models.chat import Chat, ChatAddParticipant, ChatInDb, ChatMessage, ChatMessageInCreate


router = APIRouter()


@router.post(
    "/chat/create_room",
    response_model=ChatInDb,
    tags=["chat"],
    status_code=HTTP_201_CREATED,
)
async def create_room(
        chat: Chat = Body(...), conn: AsyncIOMotorClient = Depends(get_database)
):
    result = await create_chat_room(conn, chat)
    return result


@router.post(
    "/chat/add_message",
    response_model=ChatMessage,
    tags=["chat"],
    status_code=HTTP_201_CREATED,
)
async def create_room(
        message: ChatMessageInCreate = Body(...), conn: AsyncIOMotorClient = Depends(get_database)
):
    result = await add_message(conn, message)
    return result


@router.post(
    "/chat/add_user",
    response_model=ChatMessage,
    tags=["chat"],
    status_code=HTTP_201_CREATED,
)
async def create_room(
        user_meta: ChatAddParticipant = Body(...), conn: AsyncIOMotorClient = Depends(get_database)
):
    result = await add_user_to_chat(conn, user_meta)
