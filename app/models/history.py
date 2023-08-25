from pydantic import BaseModel
import random

def generate_random_id():
    return random.randint(1, 100000)

class History(BaseModel):
    id: int = generate_random_id()
    contractId: int
    employeeId: int
    employeeName: str
    clientId: int
    clientName: str
    role: str