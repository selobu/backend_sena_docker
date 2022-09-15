from typing import Optional
from app.tools import map_name_to_table
from app.main import app
from sqlmodel import Field, SQLModel, Relationship
from pydantic import EmailStr
Tb = app.Tb
@map_name_to_table
class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombres: str
    apellidos: str
    correo: EmailStr
    cedula: str
    departamento: str
    municipio: str
    direccion: str
    activo: bool = True
    pertenecealgrupo: bool = False
    passwordid: Optional["UserInDB"] = Relationship(back_populates='user')

#    password: Optional[int] = Field(default=None, foreign_key='userindb.id')

@map_name_to_table
class UserOut(SQLModel):
    nombres: str
    apellidos: str
    correo: EmailStr
    cedula: str
    departamento: str
    municipio: str
    direccion: str
    activo: bool = True
    pertenecealgrupo: bool = False
        
@map_name_to_table
class UserInDB(SQLModel, table=True):
    id: Optional[int] = Field(
        default=None, primary_key=True, foreign_key=f'{Tb.User.__tablename__}.id')
    user: Optional["User"] = Relationship(sa_relationship_kwargs={'uselist':False},
                                          back_populates=Tb.User.__tablename__)
    hashed_password: str
