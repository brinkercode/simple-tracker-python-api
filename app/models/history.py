from pydantic import BaseModel

class History(BaseModel):
    id: int | None = None
    clientId: int
    clientName: str
    contractId: int
    employeeId: int
    employeeName: str
    role: str