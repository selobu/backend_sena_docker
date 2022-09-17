from datetime import date
from typing import Optional
from xmlrpc.client import boolean
from app.tools import map_name_to_table
from sqlmodel import Field, SQLModel, Relationship
from pydantic import EmailStr

@map_name_to_table
class TipoSolicitud(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    tipo: str


@map_name_to_table
class AtencionUsuario_register(SQLModel):
    nombrecompleto: str
    identificacion: str
    correocontacto: EmailStr
    telefonocontacto: str
    tipoSolicitud: int = Field(foreign_key='tiposolicitud.id')
    solicitud: str


@map_name_to_table
class AtencionUsuario_cierre(SQLModel):
    resuelta: Optional[bool] = False
    fechasolucion: Optional[date] = Field(default=None)
    comentarioCierre: Optional[str]


@map_name_to_table
class AtencionUsuario(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    timestamp: date = Field(default=date.today())
    usuarioencargado: Optional[int] = Field(default=None, foreign_key='user.id')
    nombrecompleto: str
    identificacion: str
    correocontacto: EmailStr
    telefonocontacto: str
    tipoSolicitud: int = Field(foreign_key='tiposolicitud.id')
    solicitud: str
    resuelta: Optional[bool] = False
    fechasolucion: Optional[date] = Field(default=None)
    comentarioCierre: Optional[str]