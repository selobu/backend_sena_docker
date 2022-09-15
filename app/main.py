# coding: utf-8
import os
try:
    os.remove("./database.db")
except:
    pass
from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from .db import UserInDB
from .fake import createusers
from .tools import  Tb, digest
from fastapi.middleware.cors import CORSMiddleware
from . import modules
from .config import settings
from sqlmodel import create_engine, SQLModel, Session, select
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
    # getting the user
    with Session(engine) as session:
        res = select(Tb.User).filter(Tb.User.correo == form_data.username)
        user = session.exec(res).first()
        if user is None:
            HTTPException(status_code=404, detail='Usuario no encontrado')
    if digest(form_data.password) != user.password:
        raise HTTPException(
            status_code=400, detail="Usuario o contraseña equivocada")

    return {"access_token": user.correo, "token_type": "bearer"}