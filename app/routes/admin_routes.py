import json
import os
from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
import requests
from fastapi.responses import RedirectResponse
from starlette import status
from app.routes.authorization_routes import get_current_admin_email
from app.schemas import admin_schemas

router = APIRouter()
url_base = os.getenv('BACKOFFICE_BASE_URL')


@router.post("/signup", response_model=admin_schemas.AdminSchema, status_code=status.HTTP_201_CREATED)
def admin_signup(user: admin_schemas.AdminSignUpSchema):
    url = url_base + "/admins/signup"
    response = requests.post(url=url, json=dict(user))
    if response.ok:
        return response.json()
    raise HTTPException(status_code=response.status_code,
                        detail=response.json()['detail'])
