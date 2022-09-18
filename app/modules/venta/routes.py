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


@router.put("/comprador/{comprador_id}", response_model=Tb.Comprador)
async def actualizar_comprador(comprador_id:int, comprador: Tb.Comprador_register):
    keys2update = list(comprador.__fields__.keys())
    keys2update = [k for k in keys2update if k !=
                   'id' and hasattr(Tb.Comprador, k)]
    with Session(engine) as session:
        res = select(Tb.Comprador).filter(Tb.Comprador.id == comprador_id)
        comp = session.exec(res).one()
        for k in keys2update:
            setattr(comp, k, getattr(comprador, k))
        session.add(comp)
        session.commit()
        session.refresh(comp)
    return comp

@router.get("/comprador/", response_model=List[Tb.Comprador])
async def leer_compradores(token=Depends(oauth2_scheme), commons=Depends(paginate_parameters)):
    limit = commons['limit']
    with Session(engine) as session:
        res = select(Tb.Comprador).limit(limit)
        res = session.exec(res).all()
    return res


@router.get("/comprador/{comprador_id}", response_model=Tb.Comprador)
async def leer_comprador(comprador_id:int,token=Depends(oauth2_scheme)):
    with Session(engine) as session:
        res = select(Tb.Comprador).filter(Tb.Comprador.id==comprador_id)
        res = session.exec(res).one()
    return res


@router.post("/carrito/{comprador_id}", response_model=Tb.Comprador)
async def compra_registrar(comprador_id: int, productos:List[int]):
    with Session(engine) as session:
        # se verifica que exista el comprador
        _res = select(Tb.Comprador).filter(Tb.Comprador.id==comprador_id)
        session.exec(_res)
        
        # se filtran los productos que existen y no esten registrados en una venta
        _res = select(Tb.Producto.id).where(Tb.Producto.id_in(productos)).\
            where(Tb.Producto.ventaid != None)
        productos = session.exec(_res).all()
        
        # se registra la compra
    return res
