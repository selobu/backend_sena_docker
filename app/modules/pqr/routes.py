from fastapi import status, Depends, HTTPException,\
    APIRouter
from fastapi.security import OAuth2PasswordBearer
# from app.fake import fake_users_db
from app.tools import paginate_parameters
from typing import Union
from app.config import settings
from app.main import app
from sqlmodel import Session, select

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

router = APIRouter(
    prefix="/Users",
    tags=["Users"],
    dependencies=[Depends(oauth2_scheme)],
    responses={404: {"description": "Not found"}},
)


Tb = settings.app.Tb
engine = settings.engine

