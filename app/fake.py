# coding:utf-8
__all__ = ['createusers']
from app.config import settings
from sqlmodel import Session, select
from app.tools import digest
from json import dumps

def createusers():
    Tb = settings.app.Tb
    default_users = [{
        "nombres": "selobu",
        "apellidos": "John Doe",
        "correo": "selobu@gmail.com",
        "cedula": "123213",
        "departamento": "Cundinamarca",
        "municipio": "cota",
        "direccion": "calle",
        "activo": True,
        "pertenecealgrupo": True,
        "password": "secret"
    },
        {
        "nombres": "johndoe",
        "apellidos": "John Doe",
        "correo": "johndoe@example.com",
        "cedula": "123214",
        "departamento": "Cundinamarca",
        "municipio": "cota",
        "direccion": "calle",
        "activo": False,
        "password": "secret"
    },
    ]
    correos= [u['correo'] for u in default_users]
    with Session(settings.engine) as session:
        not2add = select(Tb.User.correo).filter(Tb.User.correo.in_(correos))
        not2add = session.exec(not2add).all()
        # testing under heroku server
        
        toadd = [usr for usr in default_users if usr['correo'] not in not2add]
        added= []
        for user in toadd:
            user['password'] = digest(user['password'])
            added.append(Tb.User(**user))
        raise Exception(dumps(toadd))
        if len(toadd) > 0:
            session.add_all(added)
            session.commit()

def fake_hash_password(password: str):
    return "fakehashed" + password


