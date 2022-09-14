# coding: utf-8

from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from .db import UserInDB
from .fake import fake_users_db, fake_hash_password
from .tools import paginate_parameters
from . import modules

print(help(FastAPI))
app = FastAPI(
    title='Backend Sena https://github.com/selobu/backend_sena_docker', version='0.0.1',
    openapi_url='https://www.gestionhseq.com')

modules.init_app(app)

@app.get("/")
def read_root():
    return {"docs": "/docs"}


@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user_dict = fake_users_db.get(form_data.username)
    if not user_dict:
        raise HTTPException(
            status_code=400, detail="Usuaro o contraseña equivocada")
    user = UserInDB(**user_dict)
    hashed_password = fake_hash_password(form_data.password)
    if not hashed_password == user.hashed_password:
        raise HTTPException(
            status_code=400, detail="Usuario o contraseña equivocada")

    return {"access_token": user.correo, "token_type": "bearer"}