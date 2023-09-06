from pydantic import BaseModel
from typing import List

class Contract(BaseModel):
    id: int = None
    clientId: int
    type: str
    startDate: str
    endDate: str
    tech: List[str] = []
