from pydantic import BaseModel

class History(BaseModel):
    id: int
    clientId: int
    employeeId: int
    contractId: int
    employeeName: str
    clientName: str
    role: str