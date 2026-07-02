from fastapi import FastAPI 
from schemas import EventSchema, ProcessSchema
from models import ProcessEvents
from database import SessionLocal, engine, Base  
from fastapi.middleware.cors import CORSMiddleware


Base.metadata.create_all(bind=engine)


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.post("/events")
def receive_event(event: EventSchema): 
    db = SessionLocal()
    for process in event.processes:
        process_event = ProcessEvents(timestamps = event.timestamp, hostname = event.hostname, pid = process.pid, ppid = process.ppid, process_name = process.name)
        db.add(process_event)
    db.commit()
    return {"message" : "OK"}

@app.get("/events")
def show_events():
    db = SessionLocal()
    results = db.query(ProcessEvents).limit(100).all()
    return results