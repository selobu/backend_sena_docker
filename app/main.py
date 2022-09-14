from typing import Union

from fastapi import FastAPI, HTTPException, status,\
    Depends

from .db import User, UserOut
app = FastAPI()


async def paginate_parameters(
    q: Union[str, None] = None, skip: int = 0, limit: int = 20
):
    return {"q": q, "skip": skip, "limit": limit}


@app.get("/")
def read_root():
    return {"docs": "/docs"}


@app.get("/User/")
async def read_all_user(commons: dict = Depends(paginate_parameters)):
    return commons
    
@app.get("/User/{user_id}", response_model=UserOut)
async def read_user(user_id:int, q: Union[str, None]=None):
    user = User(nombres='', apellidos='',cedula='',
            correo='noreply.noreply@gestionhseq.com',
            departamento='',municipio='', direccion='')
    itemnotfound = False
    if itemnotfound:
        raise HTTPException(status_code=404, detail="Item not found")
    return user

@app.post("/User/", response_model=UserOut, status_code=status.HTTP_201_CREATED)
async def registrar_user(user: User):
    return user

@app.put("/User/{user_id}", response_model=UserOut)
async def update_user(user_id:int, user: User):
    usr = User(nombres='', apellidos='',cedula='',
            correo='noreply.noreply@gestionhseq.com',
            departamento='',municipio='', direccion='')
    return usr
