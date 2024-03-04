import logging

__logger = logging.getLogger(__name__)

def create_log(operation: str, data: dict= None, filter = None, id= None):
    operations = {
        'create': data,
        'update': {'id': id, 'data': data},
        'get': {'id': id},
        'delete': {'id': id},
        'filter': filter,
        'get_all': None
    }
    __logger.debug("Doing operation: " + operation +" -- " + str(operations[operation]))
    print("Doing operation: " + operation +" -- " + str(operations[operation]))