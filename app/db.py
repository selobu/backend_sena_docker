from typing import Union
from pydantic import BaseModel

class User(BaseModel):
        nombres: str
        apellidos: str
        password: str='123456'
        cedula: str
        departamento: str
        municipio: str
        direccion: str
        activo: bool = True
        pertenecealgrupo: bool = False