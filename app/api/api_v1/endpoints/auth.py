from app.core.config import JWT_SECRET
from app.crud.exceptions import EntityDoesNotExist
from fastapi import APIRouter, Body, Depends
from starlette.exceptions import HTTPException
from starlette.status import HTTP_201_CREATED, HTTP_202_ACCEPTED, HTTP_400_BAD_REQUEST

from ....crud.user import create_user, find_user_by_email
from ....database.mongodb import AsyncIOMotorClient, get_database
from ....models.user import UserBase, UserInCreate, UserInDb, UserInLogin, UserInResponse
from app.core.jwt import create_access_token

router = APIRouter()


@router.post(
    "/users/create",
    response_model=UserInResponse,
    tags=["authentication"],
    status_code=HTTP_201_CREATED,
)
async def register_user(
        user: UserInCreate = Body(...), conn: AsyncIOMotorClient = Depends(get_database)
):
    async with await conn.start_session() as s:
        async with s.start_transaction():
            dbuser = await create_user(conn, user)
            
            token = create_access_token(user, JWT_SECRET)
            
            return UserInResponse(
                username=dbuser.username,
                email=dbuser.email,
                avatar=dbuser.avatar,
                role_id=dbuser.role_id,
                token=token,
            )


@router.get(
    "/users/login",
    response_model=UserInResponse,
    tags=["authentication"],
    status_code=HTTP_202_ACCEPTED,
)
async def login_user(
        user: UserInLogin = Body(...), conn: AsyncIOMotorClient = Depends(get_database)
):
    try:
        user_in_db = await find_user_by_email(email=user.email)
    except EntityDoesNotExist:
        raise HTTPException(status_code=404)