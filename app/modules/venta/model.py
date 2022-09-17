from datetime import date
from typing import Optional
from xmlrpc.client import boolean
from app.tools import map_name_to_table
from sqlmodel import Field, SQLModel, Relationship
from pydantic import EmailStr
