from app.crud.pupils import create_pupil
from app.models.user import AccountData, UserInCreate
from app.crud.user import create_user, is_user_exist
from app.crud.exceptions import EntityDoesNotExist
from app.models.pupil import Pupil, PupilsAccountsInResponse, PupilsInCreate
from fastapi import APIRouter, Body, Depends
from starlette.exceptions import HTTPException
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_202_ACCEPTED, HTTP_400_BAD_REQUEST

from ....database.mongodb import AsyncIOMotorClient, get_database

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
        pupils_data: PupilsInCreate = Body(...), conn: AsyncIOMotorClient = Depends(get_database)):
    
    if pupils_data.accounts_count < 1:
        raise HTTPException(HTTP_400_BAD_REQUEST)

    accounts = []

    async with await conn.start_session() as s:
        async with s.start_transaction():
            for i in range(pupils_data.accounts_count):
                username_exist = True

                while username_exist:
                    account_username = generate_username()
                    account_password = generate_password()

                    username_exist = await is_user_exist(conn, account_username)

                dbuser = await create_user(conn, UserInCreate(email='', username=account_username, password=account_username, role_id=0))
                pupil_to_db = Pupil(user_id=dbuser.id,
                                    orphanage_id=pupils_data.orphanage_id)
                accounts.append(AccountData(
                    username=account_username, password=account_password))
                await create_pupil(conn, pupil_to_db)

    return PupilsAccountsInResponse(accounts=accounts)


@router.post(
    "/pupils/login",
    response_model=Pupil,
    tags=["pupils"],
    status_code=HTTP_202_ACCEPTED,
)
async def pupil_login(pupil: AccountData = Body(...), conn: AsyncIOMotorClient = Depends(get_database)):
    try:
        # TODO: add JWT token
        pupil_account = await find_pupil_by_username(conn, pupil.username)
        if not pupil_account.check_password(pupil.password):
            raise HTTPException(HTTP_400_BAD_REQUEST)

        return Pupil(**pupil_account.dict())

    except EntityDoesNotExist:
        raise HTTPException(status_code=404)
