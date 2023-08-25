from pydantic import BaseModel
import random
from typing import List

def generate_random_id():
    return random.randint(1, 100000)

class Contract(BaseModel):
    id: int = generate_random_id()
    clientId: int
    type: str
    startDate: str
    endDate: str
    tech: List[str]