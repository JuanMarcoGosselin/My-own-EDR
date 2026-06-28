from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


connection_url = "postgresql://juanmarcogosselingamboa@localhost:5432/edr_db"

#Create the connection by using the URL
engine = create_engine(connection_url)

SessionLocal = sessionmaker(autocommit=False, bind=engine)

#Define de Base
Base = declarative_base()

 
