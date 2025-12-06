from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, BigInteger
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from .database import Base

#Raw leads data from Meta ads ingest API
class RawLeads(Base):
    __tablename__ = "raw_leads"

    id = Column(Integer,primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    ph_number = Column(BigInteger, nullable=False)
    city = Column(String, nullable=False)
    state = Column(String, nullable=False)
    brand = Column(String, nullable=False)
    budget = Column(Integer, nullable=False)
    years_exp = Column(Integer, nullable=False)
    interest = Column(String, nullable=True)
    ad_id = Column(String, nullable=True)
    source = Column(String, nullable=True)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
    
#Leads data from ML pipeline API, converison score calculated
class Leads(Base):
    __tablename__ = "leads"

    id = Column(Integer,primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False,unique=True)
    city = Column(String, nullable=False)
    budget = Column(Integer, nullable=False)
    brand = Column(String, nullable=False)
    score = Column(Integer, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
    
# Sales team data with roles
class SalesTeam(Base):
    __tablename__ = "sales_team"
    id = Column(Integer,primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    role = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))