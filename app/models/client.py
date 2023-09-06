from pydantic import BaseModel

class Client(BaseModel):
    id: int | None = None
    name: str
    url: str | None = None
