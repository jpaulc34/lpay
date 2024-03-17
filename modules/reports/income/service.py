from abc import ABC
from annotated_types import Any

class IncomeReportService(ABC):

    def create_report(self) -> Any:
        raise NotImplementedError()