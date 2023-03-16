from pydantic import BaseModel, Field
import random
from enum import Enum
from datetime import datetime as dt 
from typing import List

def generate_random_id():
    return random.randint(1, 100000)

class Employee(BaseModel):
    id: int = generate_random_id()
    name: str
    github: str

class Client(BaseModel):
    id: int = generate_random_id()
    name: str
    url: str
    
# TODO: Enum and datetime
class Contract(BaseModel):
    id: int = generate_random_id()
    clientId: int
    type: str
    startDate: str
    endDate: str
    tech: List[str]

class History(BaseModel):
    id: int = generate_random_id()
    contractId: int
    employeeId: int
    employeeName: str
    clientId: int
    clientName: str
    role: str