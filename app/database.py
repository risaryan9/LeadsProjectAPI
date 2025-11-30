from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/fastapi"

#Creates an engine to the database (connection setup)
engine = create_engine(SQLALCHEMY_DATABASE_URL) 

#Creates a class to initilize sessions with the database (actual connections)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Base class for all other SQLAlchemy classes
Base = declarative_base()

#Function to connect with the database
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()