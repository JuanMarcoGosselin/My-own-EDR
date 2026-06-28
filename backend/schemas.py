from pydantic import BaseModel
from typing import List
from datetime import datetime

class ProcessSchema(BaseModel):
    name : str
    pid : int
    ppid : int
    

class EventSchema(BaseModel):
    hostname : str
    timestamp : datetime
    processes : List[ProcessSchema]