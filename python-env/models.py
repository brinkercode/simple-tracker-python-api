from pydantic import BaseModel
from uuid import UUID
from enum import Enum
import shortuuid
from datetime import datetime as dt 

#TODO: See if FIELD would be of use here.
class Employee(BaseModel):
    id: UUID = shortuuid.ShortUUID().random(length=22)
    name: str
    github: str

class Client(BaseModel):
    id: UUID = shortuuid.ShortUUID().random(length=22)
    name: str
    url: str

# TODO: Enum and datetime
class Contract(BaseModel):
    id: UUID = shortuuid.ShortUUID().random(length=22)
    clientId: int
    startDate: str
    endDate: str
    tech: list[str]