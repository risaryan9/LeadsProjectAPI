from fastapi import FastAPI, Response, status, HTTPException
from . import database
from . import schema

app = FastAPI()

schema.Base.metadata.create_all(bind=database.engine)