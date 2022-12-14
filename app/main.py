from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import admin_routes, authorization_routes, users_admin_routes, metrics_routes, pricing_routes

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
app.include_router(admin_routes.router,
                   prefix="/admins", tags=["Admins CRUD"])
app.include_router(users_admin_routes.router,
                   prefix="/users", tags=["User Adrministration"])
app.include_router(metrics_routes.router,
                   prefix="/metrics", tags=["Metrics"])
app.include_router(pricing_routes.router, prefix="/pricing", tags=["Pricing"])
