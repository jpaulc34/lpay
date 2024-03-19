from fastapi import APIRouter, Depends
from ...modules.tithes.service_implementation import Tithe
from ...modules.tithes.schema import TitheCreateUpdate, TitheResponse, TitheFilter
from ...modules.tithes.service import TitheService
from ...modules.auth.authenticate import UserAuth
from ...gateways.database import DatabaseGateway
from decouple import config

router = APIRouter(
        prefix="/tithes",
        tags= ["Tithes"],
        # dependencies= [Depends(UserAuth.validate_token)]
    )


__tithe_service: TitheService = Tithe(DatabaseGateway(config("tithe_collection")))

@router.get("/",response_model=list[TitheResponse])
def get_users():
    return __tithe_service.get_all()

@router.get("/filter", response_model=list[TitheResponse])
def filter_user(query: TitheFilter = Depends()):
    return __tithe_service.filter(dict(query))

@router.get("/{id}", response_model=TitheResponse)
def get_user(id: str):
    return __tithe_service.get(id)

@router.post("/", response_model=TitheResponse)
def save_user(tithe: TitheCreateUpdate):
    return __tithe_service.create(tithe)

@router.put("/{id}", response_model=TitheResponse)
def update_user(id: str, updated_tithe: TitheCreateUpdate):
    return __tithe_service.update(id, updated_tithe)

@router.delete("/{id}",response_model=TitheResponse)
def delete_user(id: str):
    return __tithe_service.delete(id)