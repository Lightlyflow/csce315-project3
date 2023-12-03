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
        self.employeeId: int = -1
        self.isManager: bool = False
        self.employeeName: str = "NO EMPLOYEE NAME"

        self.getEmployeeStatus()
        self.getUserStatus()

    def getEmployeeStatus(self) -> None:
        """Populates isEmployee, employeeID, isManager"""
        result = auth_querier.getEmployeeByEmail(self.email)

        if len(result) < 1:
            return

        self.isEmployee = True
        self.employeeId = result[0][1]
        self.isManager = result[0][2]

    def getUserStatus(self) -> None:
        result = auth_querier.getUserByEmail(self.email)

        if len(result) < 1:
            return

        self.userID = result[0][1]
        self.username = result[0][1]
