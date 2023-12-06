from .querier import execute


def clockIn(employeeID: int, activity: str):
    """Creates new row with activity and start time for employee. Time is rounded to nearest 15 minutes"""
    execute(
        f"INSERT INTO clockinout (employeeID, activity, clockin) VALUES ({employeeID}, '{activity}', round_time_quarter_hour(NOW()))")


def clockOut(employeeID: int):
    """Updates latest clockin row with clock out time. Time is rounded to nearest 15 minutes"""
    execute(f"UPDATE clockinout SET clockout=round_time_quarter_hour(NOW())"
            f"WHERE employeeid={employeeID} "
            f"AND clockin=(SELECT MAX(clockin) FROM clockinout "
            f"              WHERE employeeid={employeeID});")


def getWeek(employeeID, billingPeriod):
    return execute(f"""SELECT employeeid, clockin, clockout, activity, EXTRACT(EPOCH FROM clockout -  clockin)/3600 AS hours
        FROM clockinout
        WHERE employeeid = {employeeID} AND (clockin >= '{billingPeriod}' AND clockin <= to_timestamp('{billingPeriod}', 'YYYY-MM-DD') + INTERVAL '7' DAY);""")


# Orders
def getOrders(startDate: str):
    """Dates should be in the format YYYY-MM-DD. End date is non-inclusive"""
    return execute(
        f"SELECT orderID, employeeID, dateOrdered, price, status FROM order_table"
        f" WHERE dateordered >= '{startDate}' AND dateordered <= to_timestamp('{startDate}', 'YYYY-MM-DD') + INTERVAL '1' DAY"
        f" AND status!='fulfilled';")


def getOrderItemsByOrderID(orderID: int):
    return execute(f"SELECT m.name AS drink_name, t1.name AS topping1, t2.name AS topping2, t3.name AS topping3, "
                   f"part.sweetness AS sweetness, part.ice AS ice_level "
                   f"FROM order_part_table AS part "
                   f"LEFT JOIN menu_items_table AS m ON part.menuitemID=m.menuitemID "
                   f"LEFT JOIN topping_table AS t1 ON part.toppingID1=t1.toppingID "
                   f"LEFT JOIN topping_table AS t2 ON part.toppingID2=t2.toppingID "
                   f"LEFT JOIN topping_table AS t3 ON part.toppingID3=t3.toppingID "
                   f"WHERE part.orderID={orderID};")


def markOrder(orderID: int, status: str):
    execute(f"UPDATE order_table SET status='{status}' WHERE orderid={orderID};")
