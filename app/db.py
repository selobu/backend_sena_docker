from typing import Union
from pydantic import BaseModel, EmailStr

class User(BaseModel):
        nombres: str
        apellidos: str
        correo: EmailStr
        password: str='123456'
        cedula: str
        departamento: str
        municipio: str
        direccion: str
        activo: bool = True
        pertenecealgrupo: bool = False

# defined to hide the password
class UserOut(BaseModel):
        nombres: str
        apellidos: str
        correo: EmailStr
        cedula: str
        departamento: str
        municipio: str
        direccion: str
        activo: bool = True
        pertenecealgrupo: bool = False