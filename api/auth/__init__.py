from .auth import authBlueprint, loginManager

"""
Our submodule containing all login/logout code, as well as the login pages. 
"""

blueprint = authBlueprint
loginManager = loginManager
