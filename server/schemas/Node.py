from schemas import Role
import logging
from datetime import datetime


class Node:
    id: str
    hostname: str
    role: Role
    last_health_status: datetime

    def __init__(self, id: str, hostname: str, role: Role, last_health_status: datetime):
        self.id = id
        self.hostname = hostname
        self.role = role
        self.last_health_status = last_health_status


    def __repr__(self):
        return f"Node(id={self.id}, hostname='{self.hostname}', role={self.role})"


    # todo implement
    def report_health(self) -> bool:
        logging.info(f"Node {self.id} is checking health status")
        return self.id is not None
