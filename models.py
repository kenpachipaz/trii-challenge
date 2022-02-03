from enum import Enum

class Status(str, Enum):
    alive = "alive"
    dead = "dead"
    unknown = "unknown"