from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class RawLead(BaseModel):
    name: str
    email: EmailStr
    ph_number: str
    city: str
    state: str
    brand: str
    budget: int
    years_exp: float
    interest: str
    ad_id: str | None
    source: str = "meta_ads"