from .querier import execute


def clockIn(employeeID: int, activity: str):
    """
    Creates new row with activity and start time for employee. Time is rounded to nearest 15 minutes
    :param employeeID: employee ID
    :param activity: name of activity
    :return: None
    """
    execute(
        f"INSERT INTO clockinout (employeeID, activity, clockin) VALUES ({employeeID}, '{activity}', round_time_quarter_hour(NOW()))")


def clockOut(employeeID: int):
    """
    Updates latest clockin row with clock out time (upsert). Time is rounded to nearest 15 minutes
    :param employeeID: employee ID
    :return: None
    """
    execute(f"UPDATE clockinout SET clockout=round_time_quarter_hour(NOW())"
            f"WHERE employeeid={employeeID} "
            f"AND clockin=(SELECT MAX(clockin) FROM clockinout "
            f"              WHERE employeeid={employeeID});")


def getWeek(employeeID, billingPeriod):
    """
    Returns a week of activity for a specific employee based on their ID.
    :param employeeID: employee ID
    :param billingPeriod: start date
    :return: List containing employee ID, clock in/out times, activity name, and total hours.
    """
    return execute(f"""SELECT employeeid, clockin, clockout, activity, EXTRACT(EPOCH FROM clockout -  clockin)/3600 AS hours
        FROM clockinout
        WHERE employeeid = {employeeID} AND (clockin >= '{billingPeriod}' AND clockin <= to_timestamp('{billingPeriod}', 'YYYY-MM-DD') + INTERVAL '7' DAY);""")


# Orders
def getOrders(startDate: str):
    """
    Returns a list of unfulfilled orders for a given date
    :param startDate: date in format YYYY-MM-DD
    :return: List containing order ID, employee ID, date, price, and status
    """
    return execute(
        f"SELECT orderID, employeeID, dateOrdered, price, status FROM order_table"
        f" WHERE dateordered >= '{startDate}' AND dateordered <= to_timestamp('{startDate}', 'YYYY-MM-DD') + INTERVAL '1' DAY"
        f" AND status!='fulfilled';")


def getOrderItemsByOrderID(orderID: int):
    """
    Gets the order items comprising a single order
    :param orderID: order ID
    :return: List containing order items with item name, toppings, sweetness, and ice level
    """
    return execute(f"SELECT m.name AS drink_name, t1.name AS topping1, t2.name AS topping2, t3.name AS topping3, "
                   f"part.sweetness AS sweetness, part.ice AS ice_level "
                   f"FROM order_part_table AS part "
                   f"LEFT JOIN menu_items_table AS m ON part.menuitemID=m.menuitemID "
                   f"LEFT JOIN topping_table AS t1 ON part.toppingID1=t1.toppingID "
                   f"LEFT JOIN topping_table AS t2 ON part.toppingID2=t2.toppingID "
                   f"LEFT JOIN topping_table AS t3 ON part.toppingID3=t3.toppingID "
                   f"WHERE part.orderID={orderID};")


def markOrder(orderID: int, status: str):
    """
    Update the status of an order
    :param orderID: order ID
    :param status: new order status
    :return: None
    """
    execute(f"UPDATE order_table SET status='{status}' WHERE orderid={orderID};")
