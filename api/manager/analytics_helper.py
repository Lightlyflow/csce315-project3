from api.db import manager_querier


#Pair frequency report
def getPairReport():
    result = manager_querier.getPairReport()
    return result if result is not None else []