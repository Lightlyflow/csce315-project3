from api.db import manager_querier

#Product usage report
def getProductUsage(startDate, endDate):
    result = manager_querier.getProductUsage(startDate, endDate)
    return result if result is not None else []

#Pair frequency report
def getPairFrequency():
    result = manager_querier.getPairFrequency()
    return result if result is not None else []