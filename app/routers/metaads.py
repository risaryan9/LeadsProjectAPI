from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter

from sqlalchemy.orm import Session
from .. import  schema
from ..database import get_db
from .. import models
from ..utils import rawleadsparser



router = APIRouter()

@router.post("/leads/ingest", status_code=status.HTTP_201_CREATED)
def metaads_ingest(lead: dict, db: Session = Depends(get_db)):
    cleaned_lead = rawleadsparser.parse_meta_lead(lead)
    db_lead = schema.RawLeads(**cleaned_lead.model_dump())
    db.add(db_lead )
    db.commit()
    db.refresh(db_lead)

    return cleaned_lead
