from enum import Enum


class LogLevel(str, Enum):
    """The log levels."""

    DEBUG = "debug"
    DEFAULT = "default"
    INFO = "info"
    WARNING = "warning"
    ERROR = "error"
    CRITICAL = "critical"


LOGLEVEL: str = LogLevel.DEFAULT

FRONTEND_PORT: int = 1234
BACKEND_PORT: int = 5678
