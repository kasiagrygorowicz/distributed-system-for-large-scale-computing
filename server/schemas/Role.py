from enum import Enum, auto


class Role(Enum):
    CONTROLLER = auto()
    WORKER = auto()
