from app.models.chat import Chat, ChatAddParticipant, ChatInDb, ChatMessage, ChatMessageInCreate
from ..database.mongodb import AsyncIOMotorClient
from ..core.config import database_name, chats_collection_name
from bson.objectid import ObjectId


async def create_chat_room(conn: AsyncIOMotorClient, chat: Chat) -> ChatInDb:
    result = await conn[database_name][chats_collection_name].insert_one(chat.dict())
    chatdb = ChatInDb(**chat.dict(), id=str(result.inserted_id))
    return chatdb


async def is_user_in_chat(conn: AsyncIOMotorClient, user_id: str, chat_id: str) -> bool:
    result = await conn[database_name][chats_collection_name].find_one({'_id': ObjectId(chat_id), 'participants': user_id})
    return True if result is not None else False


async def add_message(conn: AsyncIOMotorClient, chat_message: ChatMessageInCreate) -> ChatInDb:
    message_to_db = ChatMessage(**chat_message.dict())
    if await is_user_in_chat(conn, chat_message.user_id, chat_message.chat_id):
        await conn[database_name][chats_collection_name].update_one({'_id': ObjectId(chat_message.chat_id)}, {'$push': {'messages': message_to_db.dict()}})


async def add_user_to_chat(conn: AsyncIOMotorClient, participants_data: ChatAddParticipant) -> ChatInDb:
    await conn[database_name][chats_collection_name].update_one({'_id': ObjectId(participants_data.chat_id)}, {'$push': {'participants': participants_data.user_id}})
