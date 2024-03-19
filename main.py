from fastapi import FastAPI
from .exceptions.exception_handler import ExceptionHandler
from .routes import routes
import uvicorn, os
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum

root_path = os.getenv('ENV', default='')

app = FastAPI(
    # root_path=f'/{root_path}',
    title = "FMS",
    description= "FMS api helps you manage your finances. 🚀",
    version = "0.0.1"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['0.0.0.0'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

ExceptionHandler.initiate_exception_handlers(app)

for router_module in routes:
    app.include_router(router_module.router)

handler = Mangum(app)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)