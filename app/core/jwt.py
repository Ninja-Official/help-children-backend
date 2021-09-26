from starlette.exceptions import HTTPException
import jwt

from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from datetime import datetime, timedelta
from typing import Dict
from dateutil import parser

from ..models.user import UserBase
from ..models.jwt import JWTUser, JWTMeta
from ..core.config import JWT_ACCESS_TOKEN_EXPIRE_MINUTES

from pydantic import ValidationError


JWT_SUBJECT = 'access'
JWT_ALGORITHM = 'HS256'


def create_jwt_token(
    *,
    jwt_content: Dict[str, str],
    secret_key: str,
    expires_delta: timedelta,
) -> str:
    data_to_encode = jwt_content.copy()
    expire_at = datetime.utcnow() + expires_delta
    data_to_encode.update(JWTMeta(
        expire=expire_at.isoformat(), subject=JWT_SUBJECT).dict())
    encoded = jwt.encode(data_to_encode, secret_key, algorithm=JWT_ALGORITHM)
    return encoded


def create_access_token(user: UserBase, secret_key: str) -> str:
    return create_jwt_token(
        jwt_content=JWTUser(username=user.username).dict(),
        secret_key=secret_key,
        expires_delta=timedelta(minutes=JWT_ACCESS_TOKEN_EXPIRE_MINUTES),
    )


def get_username_from_token(token: str, secret_key: str) -> str:
    try:
        return JWTUser(**jwt.decode(token, secret_key, algorithms=[JWT_ALGORITHM])).username
    except jwt.PyJWTError as decode_error:
        raise ValueError("JWT token cannot be decrypted") from decode_error
    except ValidationError as validation_error:
        raise ValueError("Malformed payload in token") from validation_error


def verify_token(token: str, secret_key: str) -> bool:
    try:
        decoded_token = jwt.decode(
            token, secret_key, algorithms=[JWT_ALGORITHM])
        expire_at = parser.parse(decoded_token['expire'])
        return True if expire_at >= datetime.utcnow() else False
    except jwt.PyJWTError as decode_error:
        raise ValueError("JWT token cannot be decrypted") from decode_error


# class JWTBearer(HTTPBearer):
#     def __init__(self, auto_error: bool = True):
#         super(JWTBearer, self).__init__(auto_error=auto_error)

#     async def __call__(self, request: Request):
#         credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
#         if credentials:
#             if not credentials.scheme == "Bearer":
#                 raise HTTPException(
#                     status_code=403, detail="Invalid authentication scheme.")
#             if not self.verify_jwt(credentials.credentials):
#                 raise HTTPException(
#                     status_code=403, detail="Invalid token or expired token.")
#             return credentials.credentials
#         else:
#             raise HTTPException(
#                 status_code=403, detail="Invalid authorization code.")

#     def verify_jwt(self, token: str) -> bool:
#         verify_token(token)
