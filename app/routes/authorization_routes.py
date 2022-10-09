import os
from pydantic import EmailStr
from app.schemas import admin_schemas, auth_schemas
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
import requests
from datetime import datetime, timedelta
from typing import Union
from starlette import status

router = APIRouter()
url_base = os.getenv('BACKOFFICE_BASE_URL')

SECRET_KEY = "0581568c0d45161280e9e97174da8b040e26d4b86526e783645c693b3a7a622f"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.post("/token", status_code=status.HTTP_200_OK)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    url = url_base + "/admins/grantaccess"

    response = requests.post(url=url, json={"email": form_data.username,
                                            "password": form_data.password})
    if not response.ok:
        raise HTTPException(status_code=response.status_code,
                            detail=response.json()['detail'])

    admin: admin_schemas.AdminSchema = response.json()
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": admin['email']}, expires_delta=access_token_expires
    )

    return {"access_token": access_token, "token_type": "bearer"}


def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
