from modules.auth import route as auth_router
from modules.users import route as user_router
from modules.tithes import route as tithe_router
from modules.reports import route as report_router

routes = [auth_router, user_router, tithe_router, report_router]