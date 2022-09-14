from fastapi import status, Depends, HTTPException
from app.db import User, UserOut, UserInDB
from fastapi.security import OAuth2PasswordBearer
from app.fake import fake_users_db
from app.tools import paginate_parameters
from typing import Union
from app.main import app

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)


def fake_decode_token(token):
    user = get_user(fake_users_db, token)
    return user


def fake_hash_password(password: str):
    return "fakehashed" + password


async def get_current_user(token: str = Depends(oauth2_scheme)):
    user = fake_decode_token(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales de autenticación inválidas",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user


async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if not current_user.activo:
        raise HTTPException(status_code=400, detail="Usuario inactivo")
    return current_user


@app.get("/User/")
async def read_all_user(commons: dict = Depends(paginate_parameters),
                        token: str = Depends(oauth2_scheme)):
    return commons


@app.get("/User/me", response_model=UserOut)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user


@app.get("/User/{user_id}", response_model=UserOut)
async def read_user(user_id: int, q: Union[str, None] = None):
    user = User(nombres='', apellidos='', cedula='',
                correo='noreply.noreply@gestionhseq.com',
                departamento='', municipio='', direccion='')
    itemnotfound = False
    if itemnotfound:
        raise HTTPException(status_code=404, detail="Item not found")
    return user


@app.post("/User/", response_model=UserOut, status_code=status.HTTP_201_CREATED)
async def registrar_user(user: User, token: str = Depends(oauth2_scheme)):
    return user


@app.put("/User/{user_id}", response_model=UserOut)
async def update_user(user_id: int, user: User, token: str = Depends(oauth2_scheme)):
    usr = User(nombres='', apellidos='', cedula='',
               correo='noreply.noreply@gestionhseq.com',
               departamento='', municipio='', direccion='')
    return usr