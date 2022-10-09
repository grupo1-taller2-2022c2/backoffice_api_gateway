from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import authorization_routes

app = FastAPI()

accept_all = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=accept_all,
    allow_credentials=True,
    allow_methods=accept_all,
    allow_headers=accept_all,
)


@app.get("/")
def read_root():
    return {"Welcome to": "Backoffice API Gateway"}


app.include_router(authorization_routes.router, tags=["Auth"])
