from fastapi import FastAPI, Response, status, HTTPException
from app import database
from app import schema
from app.routers import metaads, auth

app = FastAPI()

schema.Base.metadata.create_all(bind=database.engine)

app.include_router(metaads.router)
app.include_router(auth.router)