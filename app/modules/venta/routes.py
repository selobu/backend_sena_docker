from fastapi import status, Depends, HTTPException,\
    APIRouter
from fastapi.security import OAuth2PasswordBearer
# from app.fake import fake_users_db
from app.tools import paginate_parameters
from typing import Union, List
from app.config import settings
from app.main import app
from sqlmodel import Session, select

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

router = APIRouter(
    prefix="/ventas",
    tags=["Ventas"],
    responses={404: {"description": "Not found"}},
)


Tb = settings.app.Tb
engine = settings.engine


@router.get("/", response_model=List[Tb.Venta])
async def read_ventas(commons: dict = Depends(paginate_parameters),
                        token: str = Depends(oauth2_scheme)):
    email = token
    limit = commons['limit']
    with Session(engine) as session:
        res = select(Tb.Producto).limit(limit)
        productos = session.exec(res).all()
    return productos


@router.post("/comprador", response_model=Tb.Comprador)
async def registrar_comprador(comprador: Tb.Comprador_register):
    keys2update = list(comprador.__fields__.keys())
    keys2update = [k for k in keys2update if k !=
                   'id' and hasattr(Tb.Comprador, k)]
    with Session(engine) as session:
        req = Tb.Comprador(**dict((k, getattr(comprador, k))
                                        for k in keys2update))
        session.add(req)
        session.commit()
        session.refresh(req)
    # TODO : enviar correo con url para validar
    return req


