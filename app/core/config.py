from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()

class FitSyncBackendSettings(BaseSettings):
    HOST: str = "localhost"
    PORT: str = "8000"


class FitSyncDatabaseSettings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str
    DB_USERNAME: str
    DB_PASSWORD: str
    DB_SSL_CA: str


FITSYNC_BACKEND_SETTINGS = FitSyncBackendSettings()
FITSYNC_DATABASE_SETTINGS = FitSyncDatabaseSettings()
