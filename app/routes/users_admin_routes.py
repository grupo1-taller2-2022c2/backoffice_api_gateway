import json
import os
from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
import requests
from fastapi.responses import RedirectResponse
from starlette import status
from app.routes.authorization_routes import get_current_admin_email
from app.schemas import admin_schemas, user_schemas
from pydantic import EmailStr

router = APIRouter()
url_base = os.getenv('BACKOFFICE_BASE_URL')


@router.get("/", response_model=List[user_schemas.UserSchema], status_code=status.HTTP_200_OK)
def get_users(_admin_email: EmailStr = Depends(get_current_admin_email)):
    url = url_base + "/users/"
    response = requests.get(url=url)
    if response.ok:
        return response.json()
    raise HTTPException(status_code=response.status_code,
                        detail=response.json()['detail'])


@router.get("/passengers/{user_email}", response_model=user_schemas.PassengerSelfProfile, status_code=status.HTTP_200_OK)
def get_passenger_profile(user_email: EmailStr, _admin_email: EmailStr = Depends(get_current_admin_email)):
    url = url_base + "/users/passengers/" + user_email
    response = requests.get(url=url)
    if response.ok:
        return response.json()
    raise HTTPException(status_code=response.status_code,
                        detail=response.json()['detail'])


@router.get("/drivers/{user_email}", response_model=user_schemas.DriverSelfProfile, status_code=status.HTTP_200_OK)
def get_driver_profile(user_email: EmailStr, _admin_email: EmailStr = Depends(get_current_admin_email)):
    url = url_base + "/users/drivers/" + user_email
    response = requests.get(url=url)
    if response.ok:
        return response.json()
    raise HTTPException(status_code=response.status_code,
                        detail=response.json()['detail'])


@router.post("/blocked/{user_email}", status_code=status.HTTP_200_OK)
def block_user(user_email: EmailStr, _admin_email: EmailStr = Depends(get_current_admin_email)):
    url = url_base + "/users/blocked/" + user_email
    response = requests.post(url=url)
    if response.ok:
        return response.json()
    raise HTTPException(status_code=response.status_code,
                        detail=response.json()['detail'])


@router.post("/unblocked/{user_email}", status_code=status.HTTP_200_OK)
def unblock_user(user_email: EmailStr, _admin_email: EmailStr = Depends(get_current_admin_email)):
    url = url_base + "/users/unblocked/" + user_email
    response = requests.post(url=url)
    if response.ok:
        return response.json()
    raise HTTPException(status_code=response.status_code,
                        detail=response.json()['detail'])
