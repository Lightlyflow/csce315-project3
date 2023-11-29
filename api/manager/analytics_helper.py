from api.db import manager_querier

#Product usage report
def getProductUsage():
    result = manager_querier.getProductUsage()
    return result if result is not None else []

#Pair frequency report
def getPairFrequency():
    result = manager_querier.getPairFrequency()
    return result if result is not None else []