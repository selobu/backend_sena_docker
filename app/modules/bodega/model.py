from typing import Optional
from xmlrpc.client import boolean
from app.tools import map_name_to_table
from app.config import settings
from sqlmodel import Field, SQLModel, Relationship
from pydantic import EmailStr

Tb = settings.app.Tb


@map_name_to_table
class Ubicaciones(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    departamento: str
    centro_trabajo: str
    sitio: str

@map_name_to_table
class Producto(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    tipo: str
    responsable: Optional[int] = Field(default=None, foreign_key='user.id')
    nombre: str
    serial: str
    foto1: Optional[bytes]
    foto2: Optional[bytes]
    descripcion: str
    ubicacion: Optional[int] = Field(default=None, foreign_key='ubicaciones.id')
    activa: bool = True
