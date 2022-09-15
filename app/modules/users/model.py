from typing import Optional
from app.tools import map_name_to_table
from app.config import settings
from sqlmodel import Field, SQLModel, Relationship
from pydantic import EmailStr

Tb = settings.app.Tb


@map_name_to_table
class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombres: str
    apellidos: str
    correo: EmailStr = Field(unique=True)
    cedula: str
    departamento: str
    municipio: str
    direccion: str
    activo: bool = True
    pertenecealgrupo: bool = False
    password: str

@map_name_to_table
class UserOut(SQLModel):
    id: Optional[int]
    nombres: str
    apellidos: str
    correo: EmailStr
    cedula: str
    departamento: str
    municipio: str
    direccion: str
    activo: bool = True
    pertenecealgrupo: bool = False