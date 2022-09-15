from pydantic import BaseSettings


class Settings(BaseSettings):
    api_name: str = "Backend Sena"
    version: str = "0.0.1"
    api_description: str = "[source code](https://github.com/selobu/backend_sena_docker)"
    admin_email: str = ""
    items_per_user: int = 50
    database_uri: str = "sqlite:///database.db"
    api_contact: object = {'name': 'Sebastian López Buriticá', 'email': 'sebastian.lopez@gestionhseq.com',
                        'url': 'https://gestionhseq.com'}
    app: object
    engine: object

settings = Settings()
