from pydantic import BaseModel, EmailStr


class UserSchema(BaseModel):
    email: EmailStr
    username: str
    surname: str

    class Config:
        orm_mode = True


class PassengerSelfProfile(BaseModel):
    email: str
    username: str
    surname: str
    ratings: float


class DriverSelfProfile(BaseModel):
    email: str
    username: str
    surname: str
    ratings: float
    licence_plate: str
    model: str


class DepositFundsSchema(BaseModel):
    amount_in_ethers: str
