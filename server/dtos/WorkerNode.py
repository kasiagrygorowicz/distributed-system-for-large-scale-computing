from typing import Any

from pydantic import BaseModel


class WorkerNode(BaseModel):
    id: str
    hostname: str
