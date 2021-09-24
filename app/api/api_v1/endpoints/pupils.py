from app.crud.pupils import create_pupil, is_pupil_exist
from app.models.pupil import PupilAccount, PupilInDb, PupilsAccountsInResponse, PupilsInCreate
from app.core.config import JWT_SECRET
from app.crud.exceptions import EntityDoesNotExist
from fastapi import APIRouter, Body, Depends
from starlette.exceptions import HTTPException
from starlette.status import HTTP_201_CREATED, HTTP_202_ACCEPTED, HTTP_400_BAD_REQUEST

from ....crud.user import create_user, find_user_by_email
from ....database.mongodb import AsyncIOMotorClient, get_database
from ....models.user import UserInCreate, UserInResponse
from app.core.jwt import create_access_token

import secrets
import string

router = APIRouter()


def generate_password():
    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for i in range(8))
    return password


def generate_username():
    username = ''.join(secrets.choice(string.ascii_letters) for i in range(6))
    return username


@router.post(
    "/pupils/create-accounts",
    response_model=PupilsAccountsInResponse,
    tags=["pupils"],
    status_code=HTTP_201_CREATED,
)
async def create_pupils(
        data: PupilsInCreate = Body(...), conn: AsyncIOMotorClient = Depends(get_database)
):
    if data.accounts_count < 1:
        raise HTTPException(HTTP_400_BAD_REQUEST)

    accounts = []

    async with await conn.start_session() as s:
        async with s.start_transaction():
            for i in range(data.accounts_count):
                username_exist = True
                
                while username_exist:
                    account_username = generate_username()
                    account_password = generate_password()
                    
                    username_exist = await is_pupil_exist(conn, account_username)

                pupil_to_db = PupilInDb(
                    username=account_username, password=account_password, orphanage_id=data.orphanage_id)
                accounts.append(PupilAccount(
                    username=account_username, password=account_password))
                await create_pupil(conn, pupil_to_db)

    return PupilsAccountsInResponse(accounts=accounts)
