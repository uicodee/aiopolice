from enum import Enum


class Status(Enum):
    APPROVE = "approve"
    REJECT = "reject"


class Role(Enum):
    SUPERADMIN = "superadmin"
    ADMIN = "admin"
    USER = "user"

