from fastapi import APIRouter, Depends
from modules.reports.income.service_implementation import IncomeReport
from modules.reports.income.service import IncomeReportService
from modules.auth.authenticate import UserAuth
from gateways.database import DatabaseGateway
from decouple import config
from datetime import datetime


# quick debug
from config.database import Database
from pydantic import BaseModel, EmailStr, model_validator, Field, validator, model_validator


router = APIRouter(
        prefix="/reports",
        tags= ["Reports"],
        # dependencies= [Depends(UserAuth.validate_token)]
    )

class IncomeReportFilter(BaseModel):
    date: str

# INCOME
__report_service: IncomeReportService = IncomeReport(DatabaseGateway(config("report_collection")))

@router.get("/income")
def create_report(date: str):
    data = {'date':date}
    tithes_data = Database.collection(config("tithe_collection")).find(data)

    # sixAm = sum([int(value['amount']) for value in tithes_data if value['service'] == '6am'])
    # nineAm = sum([int(value['amount']) for value in tithes_data if value['service'] == '9am'])
    sixAm = []
    nineAm = []
    for i in tithes_data:
        if i['service'] == '6am':
            print('appended', i['service'], i['amount'])
        else:
            print('appended', i['service'], i['amount'])
    sum6 = sum(sixAm)
    sum9 = sum(nineAm)
    total = sum6+sum9
    date = datetime.strptime(date, '%Y-%m-%d')

    serialized = {
        'month': date.strftime('%B %Y'),
        'date': date.strftime('%d'),
        'sixAm': sum6,
        'nineAm': sum9,
        'total': total,
        'tithes_of_tithes': round(total*0.10, 2)
    }

    return serialized
    # return __report_service.create_report()