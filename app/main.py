# coding: utf-8

from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from .db import UserInDB
from .fake import createusers
from .tools import  Tb
from fastapi.middleware.cors import CORSMiddleware
from . import modules
from .config import settings
from sqlmodel import create_engine, SQLModel
# print(help(FastAPI))
app = FastAPI(
    title= settings.api_name,
    version= settings.version,
    description= settings.api_description,
    contact= settings.api_contact,
    license_info={'name': 'GPL V3',
                  'url': 'https://www.gnu.org/licenses/gpl-3.0.en.html'})

# making app globally available by calling settings
settings.app = app
setattr(app,'Tb', Tb)

modules.init_app(app)


engine = create_engine(settings.database_uri) # creating an sqlite database
settings.engine = engine
# ---------------------------------------------
# to be used onle once when database is created
SQLModel.metadata.create_all(engine)
createusers()
# ---------------------------------------------

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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