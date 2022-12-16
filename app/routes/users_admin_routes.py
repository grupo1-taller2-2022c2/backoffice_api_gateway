import json
import os
from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
import requests
from fastapi.responses import RedirectResponse
from starlette import status
from app.routes.authorization_routes import get_current_admin_email
from app.schemas import admin_schemas, user_schemas
from app.schemas.user_schemas import *
from pydantic import EmailStr

router = APIRouter()
url_base = os.getenv("BACKOFFICE_BASE_URL")
wallets_url_base = os.getenv("WALLETS_BASE_URL")
users_be_url = os.getenv("USERS_BASE_URL")


@router.get(
    "/", response_model=List[user_schemas.UserFullInfo], status_code=status.HTTP_200_OK
)
def get_users(_admin_email: EmailStr = Depends(get_current_admin_email)):
    url = url_base + "/users/"
    response = requests.get(url=url)
    if response.ok:
        return response.json()
    raise HTTPException(
        status_code=response.status_code, detail=response.json()["detail"]
    )


@router.get(
    "/passengers/{user_email}",
    response_model=user_schemas.PassengerSelfProfile,
    status_code=status.HTTP_200_OK,
)
def get_passenger_profile(
    user_email: EmailStr, _admin_email: EmailStr = Depends(get_current_admin_email)
):
    url = url_base + "/users/passengers/" + user_email
    response = requests.get(url=url)
    if response.ok:
        return response.json()
    raise HTTPException(
        status_code=response.status_code, detail=response.json()["detail"]
    )


@router.get(
    "/drivers/{user_email}",
    response_model=user_schemas.DriverSelfProfile,
    status_code=status.HTTP_200_OK,
)
def get_driver_profile(
    user_email: EmailStr, _admin_email: EmailStr = Depends(get_current_admin_email)
):
    url = url_base + "/users/drivers/" + user_email
    response = requests.get(url=url)
    if response.ok:
        return response.json()
    raise HTTPException(
        status_code=response.status_code, detail=response.json()["detail"]
    )


@router.post("/blocked/{user_email}", status_code=status.HTTP_200_OK)
def block_user(
    user_email: EmailStr, _admin_email: EmailStr = Depends(get_current_admin_email)
):
    url = url_base + "/users/blocked/" + user_email
    response = requests.post(url=url)
    if response.ok:
        return response.json()
    raise HTTPException(
        status_code=response.status_code, detail=response.json()["detail"]
    )


@router.post("/unblocked/{user_email}", status_code=status.HTTP_200_OK)
def unblock_user(
    user_email: EmailStr, _admin_email: EmailStr = Depends(get_current_admin_email)
):
    url = url_base + "/users/unblocked/" + user_email
    response = requests.post(url=url)
    if response.ok:
        return response.json()
    raise HTTPException(
        status_code=response.status_code, detail=response.json()["detail"]
    )


@router.get("/{user_email}/wallet", status_code=status.HTTP_200_OK)
def get_user_wallet(
    user_email: EmailStr,
    _admin_email: EmailStr = Depends(get_current_admin_email),
):
    url = url_base + "/users/" + user_email + "/wallet"
    response = requests.get(url=url)
    if response.ok:
        return response.json()
    raise HTTPException(
        status_code=response.status_code, detail=response.json()["detail"]
    )


@router.post("/{user_email}/wallet/deposit", status_code=status.HTTP_200_OK)
def deposit_funds_in_user_wallet(
    user_email: EmailStr,
    deposit_funds: user_schemas.DepositFundsSchema,
    _admin_email: EmailStr = Depends(get_current_admin_email),
):
    url = url_base + "/users/" + user_email + "/wallet/deposit"
    body = {"amount_in_ethers": deposit_funds.amount_in_ethers}
    response = requests.post(url=url, json=body)

    if response.ok:
        return response.json()

    raise HTTPException(
        status_code=response.status_code, detail=response.json()["detail"]
    )


@router.get("/systemwallet", status_code=status.HTTP_200_OK)
def get_system_wallet(_admin_email: EmailStr = Depends(get_current_admin_email)):
    url = wallets_url_base + "/wallets/system"
    response = requests.get(url=url)

    if response.ok:
        return response.json()

    raise HTTPException(
        status_code=response.status_code, detail=response.json()["detail"]
    )


@router.delete("/drivers/reports", status_code=status.HTTP_200_OK)
def delete_report_with_report_id(report: ReportDelete):
    url = users_be_url + "/drivers/reports"
    response = requests.delete(url=url, json=dict(report))
    if response.ok:
        return response.json()
    raise HTTPException(
        status_code=response.status_code, detail=response.json()["detail"]
    )


@router.get("/drivers/reports/all", status_code=status.HTTP_200_OK)
def get_drivers_reports():
    url = users_be_url + "/drivers/reports/all"
    response = requests.get(url=url)
    if response.ok:
        return response.json()
    raise HTTPException(
        status_code=response.status_code, detail=response.json()["detail"]
