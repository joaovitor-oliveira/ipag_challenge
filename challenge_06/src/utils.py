from enum import Enum


class Priority(Enum):
    HIGH = 1
    MEDIUM = 2
    LOW = 3


class Status(Enum):
    PENDING = 1
    DONE = 2
