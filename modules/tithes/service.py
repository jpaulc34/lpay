from abc import ABC
from ...modules.tithes.schema import TitheResponse

class TitheService(ABC):
    
    def create(self) -> TitheResponse:
        raise NotImplementedError()

    def update(self, id : str) -> TitheResponse:
        raise NotImplementedError()

    def delete(self, id : str) -> TitheResponse:
        raise NotImplementedError()

    def filter(self, filter : dict) -> list[TitheResponse]:
        raise NotImplementedError()

    def get_all() -> list[TitheResponse]:
        raise NotImplementedError()

    def get(self, id : str) -> TitheResponse:
        raise NotImplementedError()