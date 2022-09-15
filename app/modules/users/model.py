from typing import Optional

from sqlmodel import Field, SQLModel
from pydantic import EmailStr


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombres: str
    apellidos: str
    correo: EmailStr
    password: str = '123456'
    cedula: str
    departamento: str
    municipio: str
    direccion: str
    activo: bool = True
    pertenecealgrupo: bool = False
    
