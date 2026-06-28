from fastapi import FastAPI 
from schemas import EventSchema, ProcessSchema
from models import ProcessEvents
from database import SessionLocal, engine, Base  


Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/events")
def receive_event(event: EventSchema): 
    db = SessionLocal()
    for process in event.processes:
        process_event = ProcessEvents(timestamps = event.timestamp, hostname = event.hostname, pid = process.pid, ppid = process.ppid, process_name = process.name)
        db.add(process_event)
    db.commit()
    return {"message" : "OK"}
