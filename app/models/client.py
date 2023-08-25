from pydantic import BaseModel
import random

def generate_random_id():
    return random.randint(1, 100000)

class Client(BaseModel):
    class Config:
        underscore_attrs_are_private = True
    _id: int = generate_random_id()
    name: str
    url: str