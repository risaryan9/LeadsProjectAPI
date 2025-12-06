from datetime import datetime, timedelta
from . import schema, database, models
from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')


SECRET_KEY = "trishu123"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

def create_jwt_token(data :dict):
    encode_data = data.copy()

    exp_time = datetime.now() + timedelta(minutes = ACCESS_TOKEN_EXPIRE_MINUTES)
    encode_data.update({"exp" : exp_time})

    encoded_jwt = jwt.encode(encode_data,SECRET_KEY,ALGORITHM)
    return encoded_jwt