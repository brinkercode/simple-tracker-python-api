from pydantic import BaseModel

class Employee(BaseModel):
    id: int | None = None
    name: str
    github: str