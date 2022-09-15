# coding: utf-8

from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from .db import UserInDB
from .fake import fake_users_db, fake_hash_password
from .tools import paginate_parameters, Tb
from fastapi.middleware.cors import CORSMiddleware
from . import modules
from sqlmodel import create_engine, SQLModel
# print(help(FastAPI))
app = FastAPI(
    title='Backend Sena',
    version='0.0.1',
    description='[source code](https://github.com/selobu/backend_sena_docker)',
    contact={'name': 'Sebastian López Buriticá', 'email': 'sebastian.lopez@gestionhseq.com',
             'url':'https://gestionhseq.com'},
    license_info={'name': 'GPL V3',
                  'url': 'https://www.gnu.org/licenses/gpl-3.0.en.html'})

setattr(app,'Tb', Tb)

modules.init_app(app)

engine = create_engine("sqlite:///database.db") # creating an sqlite database

SQLModel.metadata.create_all(engine)

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