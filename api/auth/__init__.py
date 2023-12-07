"""
Our submodule containing all login/logout code, as well as the login pages.
blueprint contains all auth endpoints.
"""

from .auth import authBlueprint, loginManager


blueprint = authBlueprint
loginManager = loginManager
