from logging.config import dictConfig
import logging
from ..config.log import LogConfig

dictConfig(LogConfig().model_dump())
logger = logging.getLogger("FMS")
# logger.info("Dummy Info")
# logger.error("Dummy Error")
# logger.debug("Dummy Debug")
# logger.warning("Dummy Warning")

def create_log_operation(operation: str, data: dict= None, filter = None, id= None):
    # logger.debug("Dummy Debug")
    operations = {
        'create': data,
        'update': {'id': id, 'data': data},
        'get': {'id': id},
        'delete': {'id': id},
        'filter': filter,
        'get_all': None
    }
    logger.debug(operation.upper() +" -- " + str(operations[operation]))

def database_error(message):
    logger.error("Failed to connect to database: %s", message, exc_info=True)
    exit(1)
