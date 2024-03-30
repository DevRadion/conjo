from enum import Enum


class ReturnCode(Enum):
    SUCCESS = 0
    ERROR = 1
    PermissionError = 100

    def __str__(self):
        match self:
            case 0:
                "Success"
            case 100:
                "PermissionError"
