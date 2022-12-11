from typing import Union

from pydantic import BaseModel, EmailStr


class UserSchema(BaseModel):
    email: EmailStr
    username: str
    surname: str
    blocked: bool

    class Config:
        orm_mode = True


class DriverInfo(BaseModel):
    ratings: float
    licence_plate: str
    model: str


class UserFullInfo(BaseModel):
    email: EmailStr
    username: str
    surname: str
    blocked: bool
    ratings: float
    driver: Union[DriverInfo, None]

    class Config:
        orm_mode = True


class PassengerSelfProfile(BaseModel):
    email: str
    username: str
    surname: str
    ratings: float
    photo: str


class DriverSelfProfile(BaseModel):
    email: str
    username: str
    surname: str
    ratings: float
    licence_plate: str
    model: str
    photo: str


class DepositFundsSchema(BaseModel):
    amount_in_ethers: str
