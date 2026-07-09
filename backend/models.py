from database import Base
from sqlalchemy import Column, Integer, String, DateTime

class ProcessEvents(Base): 
    __tablename__ = "process_events"
    id = Column(Integer, primary_key=True)
    timestamps = Column(DateTime)
    process_name = Column(String)
    pid = Column(Integer)
    ppid = Column(Integer)
    hostname = Column(String)

 

