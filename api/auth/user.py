from flask_login import UserMixin


class User(UserMixin):
    def __init__(self, _id: int, _username: str, _email: str, _isEmployee: bool = False, _isManager: bool = False):
        super(User, self).__init__()
        self.id = str(_id)
        self.email = _email
        self.username = _username
        self.isEmployee = _isEmployee
        self.isManager = _isManager
