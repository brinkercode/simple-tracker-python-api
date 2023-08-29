from pydantic import BaseModel

class Client(BaseModel):
    id: int
    name: str
    url: str | None = None