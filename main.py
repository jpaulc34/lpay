from fastapi import FastAPI
from users.route import user_router
from auth.route import auth_router

app = FastAPI(
    title = "FMS",
    description= "FMS api helps you manage your finances. 🚀",
    version = "0.0.1"
)

app.include_router(router=auth_router)
app.include_router(router=user_router)