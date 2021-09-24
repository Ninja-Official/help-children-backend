from fastapi import APIRouter, Body, Depends
from starlette.exceptions import HTTPException
from starlette.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST

from ....crud.user import create_user
from ....database.mongodb import AsyncIOMotorClient, get_database
from ....models.user import UserBase, UserInCreate, UserInDb

router = APIRouter()


@router.post(
    "/users/create",
    response_model=UserInDb,
    tags=["authentication"],
    status_code=HTTP_201_CREATED,
)
async def register_user(
        user: UserInCreate = Body(...), conn: AsyncIOMotorClient = Depends(get_database)
):
    async with await conn.start_session() as s:
        async with s.start_transaction():
            dbuser = await create_user(conn, user)
            return dbuser
