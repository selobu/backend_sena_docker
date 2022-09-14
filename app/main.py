from typing import Union

from fastapi import FastAPI
from .db import User, UserOut
app = FastAPI()


@app.get("/")
def read_root():
    return {"docs": "/docs"}

@app.get("/User/{user_id}", response_model=UserOut)
async def read_user(user_id:int, q: Union[str, None]=None):
    user = User(nombres='', apellidos='',cedula='',
            correo='noreply.noreply@gestionhseq.com',
            departamento='',municipio='', direccion='')
    return user

@app.post("/User/", response_model=UserOut)
async def registrar_user(user: User):
    return user

@app.put("/User/{user_id}", response_model=UserOut)
async def update_user(user_id:int, user: User):
    usr = User(nombres='', apellidos='',cedula='',
            correo='noreply.noreply@gestionhseq.com',
            departamento='',municipio='', direccion='')
    return usr