from pydantic import BaseModel

class Client(BaseModel):
    _id: int = None
    name: str
    url: str | None = None