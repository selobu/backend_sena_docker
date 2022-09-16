from fastapi import status, Depends, HTTPException, \
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
    prefix="/Producto",
    tags=["Producto"],
    dependencies=[Depends(oauth2_scheme)],
    responses={404: {"description": "Not found"}},
)

Tb = settings.app.Tb
engine = settings.engine


@router.get("/", response_model=Tb.Producto)
async def read_products(commons: dict = Depends(paginate_parameters),
    token: str = Depends(oauth2_scheme)):
    email = token
    limit = commons['limit']
    with Session(engine) as session:
        res = select(Tb.Producto).limit(limit)
        productos = session.exec(res).all()
    return productos


@router.get("/{product_id}", response_model=Tb.UserOut)
async def read_product_by_id(product_id:int, token: str = Depends(oauth2_scheme), q: Union[str, None] = None):
    with Session(engine) as session:
        res = select(Tb.User).filter(Tb.User.correo == 1)
        user = session.exec(res).one()
    return user
