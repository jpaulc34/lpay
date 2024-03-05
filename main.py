from fastapi import FastAPI
from exceptions.exception_handler import ExceptionHandler
from routers import routes

app = FastAPI(
    title = "FMS",
    description= "FMS api helps you manage your finances. 🚀",
    version = "0.0.1"
)
ExceptionHandler.initiate_exception_handlers(app)

for router_module in routes:
    app.include_router(router_module.router)