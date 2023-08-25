from pydantic import BaseModel

class Employee(BaseModel):
    name: str
    github: str
    _id: int = None