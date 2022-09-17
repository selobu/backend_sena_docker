from datetime import date
from typing import Optional
from xmlrpc.client import boolean
from app.tools import map_name_to_table
from sqlmodel import Field, SQLModel, Relationship
from pydantic import EmailStr

@map_name_to_table
class Ventas(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    