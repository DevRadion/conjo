import enum


class Level(enum.Enum):
    VERBOSE = "VERBOSE"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"
    TRACE = "TRACE"

    @property
    def id(self):
        match self:
            case Level.VERBOSE:
                return 0
            case Level.INFO:
                return 1
            case Level.WARNING:
                return 2
            case Level.ERROR:
                return 3
            case Level.CRITICAL:
                return 4
            case Level.TRACE:
                return 5
