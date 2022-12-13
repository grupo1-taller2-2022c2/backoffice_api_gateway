import json
import os
from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
import requests
from fastapi.responses import RedirectResponse
from starlette import status
from app.schemas.pricing_schemas import PriceChange
from app.routes.authorization_routes import get_current_admin_email
from pydantic import EmailStr

router = APIRouter()
url_base = os.getenv('TRIPS_BASE_URL')


@router.patch("/cost/", status_code=status.HTTP_200_OK)
def modify_cost_rule(price_change: PriceChange, _admin_email: EmailStr = Depends(get_current_admin_email)):
    """Modify rules, if 0 then it doesn't change. The days of week can be 'Monday', 'Tuesday', 'Wednesday', etc.
    Busy hours can be from 0 to 24."""
    url = url_base + "/trips/cost/"
    response = requests.patch(url=url, json=dict(price_change))
    if response.ok:
        return response.json()
    raise HTTPException(status_code=response.status_code,
                        detail=response.json()['detail'])


@router.get("/", status_code=status.HTTP_200_OK)
def get_pricing(_admin_email: EmailStr = Depends(get_current_admin_email)):
    url = url_base + "/trips/pricing/"
    response = requests.get(url=url)
    if response.ok:
        return response.json()
    raise HTTPException(status_code=response.status_code,
                        detail=response.json()['detail'])
