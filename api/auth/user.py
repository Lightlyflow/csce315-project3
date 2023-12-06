from flask_login import UserMixin
from api.db import auth_querier


class User(UserMixin):
    """A user that exists as an employee or a user. Email is the main identifier. ASSUMES EMAIL EXISTS!!!"""
    def __init__(self, _email: str):
        super(User, self).__init__()
        self.id: str = str(_email)

        # User Stats
        self.userID: int = -1
        self.email: str = _email
        self.username: str = "NO USERNAME"

        # Employee Stats
        self.isEmployee: bool = False
        self.isManager: bool = False
        self.isAdmin: bool = False
        self.employeeId: int = -1
        self.employeeName: str = "NO EMPLOYEE NAME"
        self.preferredName: str = "NO PREFERRED NAME"

        self.getEmployeeStatus()
        self.getUserStatus()

    def getEmployeeStatus(self) -> None:
        """Populates isEmployee, employeeID, isManager"""
        result = auth_querier.getEmployeeByEmail(self.email)

        if result is None or len(result) < 1:
            return

        self.isEmployee = True
        self.employeeName = result[0][0]
        self.employeeId = result[0][1]
        self.isManager = result[0][2]
        self.preferredName = result[0][3] if result[0][3] != "" else self.employeeName
        self.isAdmin = result[0][4]

    def getUserStatus(self) -> None:
        result = auth_querier.getUserByEmail(self.email)

        if result is None or len(result) < 1:
            return

        self.userID = result[0][1]
        self.username = result[0][1]
