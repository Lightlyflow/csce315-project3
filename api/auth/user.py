from flask_login import UserMixin
from api.db import auth_querier


class User(UserMixin):
    def __init__(self, _id: int, _username: str, _email: str, _employeeID: int | None = None):
        super(User, self).__init__()
        self.id = str(_id)
        self.email = _email
        self.username = _username
        self.isEmployee = bool(_employeeID)
        self.employeeId = _employeeID
        self.isManager = self.getManagerStatus()

    def getEmployeeInfo(self):
        # TODO :: FINISH THIS, REMOVE getManagerStatus()
        pass

    def getManagerStatus(self) -> bool:
        if self.employeeId is None:
            return False
        result = auth_querier.getEmployeeById(self.employeeId)
        if result[0][2]:
            return True
        return False
