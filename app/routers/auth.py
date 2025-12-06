from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter

from sqlalchemy.orm import Session
from .. import  schema
from ..database import get_db
from .. import models
from ..utils import rawleadsparser, authutils
from .. import authlogic


router = APIRouter()

@router.post("/login", status_code=status.HTTP_202_ACCEPTED)
def loginroute(userdata: dict, db: Session = Depends(get_db)):
    user = db.query(schema.SalesTeam).filter(schema.SalesTeam.email == userdata["email"]).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials")
    
    if not authutils.verify(userdata["password  "],user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials")
    
    access_token = authlogic.create_jwt_token(data={"user_id":user.id,"role":user.role})

    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/register",status_code=status.HTTP_201_CREATED)
def registeruser(userdata: dict, db: Session = Depends(get_db)):
    user = db.query(schema.SalesTeam).filter(schema.SalesTeam.email == userdata["email"]).first()
    
    if user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"You already have a account, please login instead")
    
    user = schema.SalesTeam(**userdata)
    user.password = authutils.hash(user.password)

    db.add(user)
    db.commit()
    db.refresh(user)

    return user