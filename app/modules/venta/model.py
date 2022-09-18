from datetime import date
from typing import Optional
from xmlrpc.client import boolean
from app.tools import map_name_to_table
from sqlmodel import Field, SQLModel, Relationship
from pydantic import EmailStr


@map_name_to_table
class Comprador_register(SQLModel):
    nombrecompleto: str
    cedula: str
    direccionResidencia: str
    departamento: str
    municipio: str
    direccionEnvio: str
    correo: EmailStr
    telefono: str


@map_name_to_table
class Comprador(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombrecompleto: str
    cedula: str
    direccionResidencia: str
    departamento: str
    municipio: str
    direccionEnvio: str
    correo: EmailStr
    telefono: str
    correovalidado: Optional[bool] = False


@map_name_to_table
class Venta(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    comprador: int = Field(foreign_key='comprador.id')
    fechacompra: Optional[date] = Field(default=date.today())
    responsableEnviar: Optional[int] = Field(default=None, foreign_key='user.id')
    enviado: Optional[bool] = False
    fechaEnvio: Optional[date] = Field(default=None)
    recibido: Optional[bool] = False
    facturar: Optional[bool] = False # la facuración se envía al correo electrónico descrito
    cancelada: Optional[bool] = False