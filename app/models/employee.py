from pydantic import BaseModel

class Employee(BaseModel):
    name: str
    github: str
    id: int | None = None