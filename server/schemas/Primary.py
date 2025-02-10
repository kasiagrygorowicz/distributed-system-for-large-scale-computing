import logging
from datetime import datetime

from schemas.Node import Node
from schemas.Role import Role


class Primary:
    nodes: dict[str, Node] = {}

    def __repr__(self):
        return f"Primary(nodes={self.nodes})"

    def check_for_new_nodes(self):
        logging.info("Checking for new nodes")

    def add_worker(self, id: str, hostname: str):
        logging.info(f"Registering new worker: {id}, {hostname}")
        self.nodes[id] = Node(id, hostname, Role.WORKER, datetime.now())
        return True

