from api.db import manager_querier

#Product usage report
def getProductUsage(startDate, endDate):
    """Calls the querier and returns the result of the product usage query"""
    result = manager_querier.getProductUsage(startDate, endDate)
    return result if result is not None else []

#Sales report
def getSalesHistory(startDate, endDate):
    """Calls the querier and returns the result of the sales history query"""
    result = manager_querier.getSalesHistory(startDate, endDate)
    return result if result is not None else []

#Excess report
def getExcessItems(startDate):
    """Calls the querier and returns the result of the excess items query"""
    result = manager_querier.getExcessItems(startDate)
    return result if result is not None else []

#Pair frequency report
def getPairFrequency(startDate, endDate):
    """Calls the querier and returns the result of the pair frequency query"""
    result = manager_querier.getPairFrequency(startDate, endDate)
    return result if result is not None else []