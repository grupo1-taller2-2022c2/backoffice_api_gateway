from pydantic import BaseModel, EmailStr

#######################################################################


class AdminSignUpSchema(BaseModel):
    email: EmailStr
    password: str
    username: str
    surname: str


class AdminSchema(BaseModel):
    email: EmailStr
    username: str
    surname: str
