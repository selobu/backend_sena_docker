from typing import Union

from fastapi import FastAPI
from .db import User
app = FastAPI()


@app.get("/")
def read_root():
    return {"docs": "/docs"}

@app.get("/User/{user_id}", response_model=User)
async def read_user(user_id:int, q: Union[str, None]=None):
    usr = User(nombres='', apellidos='',cedula='',
              departamento='',municipio='', direccion='')
    return usr

@app.post("/User/", response_model=User)
async def registrar_user(user: User):
    return user

@app.put("/User/{user_id}", response_model=User)
async def update_user(user_id:int, user: User):
    usr = User(nombres='', apellidos='',cedula='',
              departamento='',municipio='', direccion='')
    return usr