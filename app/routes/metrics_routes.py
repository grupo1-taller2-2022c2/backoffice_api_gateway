import datetime
import os
from fastapi import APIRouter, HTTPException, status, Query, Depends
from starlette import status
import requests
from app.routes.authorization_routes import get_current_admin_email
from pydantic import EmailStr

router = APIRouter()
url_base = os.getenv('BACKOFFICE_BASE_URL')


@router.get("/registrations", status_code=status.HTTP_200_OK)
def get_registrations_count(method: str = Query(default="mailpassword", description="Should be mailpassword or federatedidentity"),
                            from_date: datetime.date = datetime.date.today(), _admin_email: EmailStr = Depends(get_current_admin_email)):

    url = url_base + "/metrics/registrations?method=" + \
        method + "&from_date=" + str(from_date)
    response = requests.get(url=url)
    if response.ok:
        return response.json()
    raise HTTPException(status_code=response.status_code,
                        detail=response.json()['detail'])


@router.get("/logins", status_code=status.HTTP_200_OK)
def get_logins_count(method: str = Query(default="mailpassword", description="Should be mailpassword or federatedidentity"),
                     from_date: datetime.date = datetime.date.today(), _admin_email: EmailStr = Depends(get_current_admin_email)):

    url = url_base + "/metrics/logins?method=" + \
        method + "&from_date=" + str(from_date)
    response = requests.get(url=url)
    if response.ok:
        return response.json()
    raise HTTPException(status_code=response.status_code,
                        detail=response.json()['detail'])


@router.get("/blocked_users", status_code=status.HTTP_200_OK)
def get_current_blocked_users_count(_admin_email: EmailStr = Depends(get_current_admin_email)):
    url = url_base + "/metrics/blocked_users"
    response = requests.get(url=url)
    if response.ok:
        return response.json()
    raise HTTPException(status_code=response.status_code,
                        detail=response.json()['detail'])
