from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter

from sqlalchemy.orm import Session
from .. import  schemas
from ..database import get_db


router = APIRouter()

@router.post("/leads/ingest")
def metaads_ingest(db: Session = Depends(get_db)):
    return