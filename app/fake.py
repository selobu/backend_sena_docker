# ------------------- to bew replaced 
fake_users_db = {
    "selobu@gmail.com": {
        "nombres": "selobu",
        "apellidos": "John Doe",
        "correo": "selobu@gmail.com",
        "hashed_password":  "fakehashedsecret",
        "cedula": "123213",
        "departamento": "Cundinamarca",
        "municipio": "cota",
        "direccion": "calle",
        "activo": True
    },
    "johndoe@example.com": {
        "nombres": "johndoe",
        "apellidos": "John Doe",
        "correo": "johndoe@example.com",
        "hashed_password": "fakehashedsecret2",
        "cedula": "123214",
        "departamento": "Cundinamarca",
        "municipio": "cota",
        "direccion": "calle",
        "activo": False
    },
}
# --------------------


def fake_hash_password(password: str):
    return "fakehashed" + password
