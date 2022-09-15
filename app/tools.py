# coding:utf-8
import hashlib
from typing import Union

def digest(text):
    if isinstance(text, str):
        text = bytearray(text, 'utf-8')
    hash_object = hashlib.sha256(text)
    return hash_object.hexdigest()

async def paginate_parameters(
    q: Union[str, None] = None, skip: int = 0, limit: int = 20
):
    return {"q": q, "skip": skip, "limit": limit}


class TbContainer(object):
    pass

# punto comun para acceder a las tablas
Tb = TbContainer()


def map_name_to_table(cls):
    #globals()[clase.__name__] = clase
    # table_mappers['Tb'+clase.__name__] = clase
    if hasattr(Tb, cls.__name__):
        raise Exception(f'ya esta declarada la tabla {cls.__name__}')
    setattr(Tb, cls.__name__, cls)