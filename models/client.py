from sqlalchemy import Column, String, Text
from models.base import BaseModel


class Client(BaseModel):
    """Client model."""
    __tablename__ = "clients"
    
    name = Column(String(100), nullable=False)
    email = Column(String(255), unique=True, nullable=False, index=True)
    phone = Column(String(20), nullable=True)
    address = Column(Text, nullable=True)