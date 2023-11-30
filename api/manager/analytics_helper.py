from api.db import manager_querier

#Product usage report
def getProductUsage(startDate, endDate):
    result = manager_querier.getProductUsage(startDate, endDate)
    return result if result is not None else []

#Pair frequency report
def getPairFrequency(startDate, endDate):
    result = manager_querier.getPairFrequency(startDate, endDate)
    return result if result is not None else []