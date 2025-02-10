from dataclasses import dataclass


@dataclass
class HealthStatus:
    id: int
    hostname: str
    status: str
