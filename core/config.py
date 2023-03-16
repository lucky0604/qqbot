import os
from pydantic import BaseSettings


class Config(BaseSettings):
    ENV: str = "development"
    DEBUG: bool = True
    APP_HOST: str = "0.0.0.0"
    APP_PORT: int = 3000
    WRITER_DB_URL: str = f"mysql+aiomysql://root:123456@localhost:3306/qqbot"
    READER_DB_URL: str = f"mysql+aiomysql://root:123456@localhost:3306/qqbot"
    JWT_SECRET_KEY: str = "fastapi"
    JWT_ALGORITHM: str = "HS256"
    SENTRY_SON: str = None
    CELERY_BROKER_URL: str = "ampq://user:bitnami@localhost:5672/"
    CELERY_BACKEND_URL: str = "redis://localhost:6379/2"
    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379


class DevelopmentConfig(Config):
    WRITER_DB_URL: str = f"mysql+aiomysql://root:123456@db:3306/qqbot"
    READER_DB_URL: str = f"mysql+aiomysql://root:123456@db:3306/qqbot"
    REDIS_HOST: str = "redis"
    REDIS_PORT: int = 6379


class LocalConfig(Config):
    WRITER_DB_URL: str = f"mysql+aiomysql://fastapi:fastapi@localhost:3306/fastapi"
    READER_DB_URL: str = f"mysql+aiomysql://fastapi:fastapi@localhost:3306/fastapi"


class ProductionConfig(Config):
    DEBUG: str = False
    WRITER_DB_URL: str = f"mysql+aiomysql://fastapi:fastapi@localhost:3306/prod"
    READER_DB_URL: str = f"mysql+aiomysql://fastapi:fastapi@localhost:3306/prod"


def get_config():
    env = os.getenv("ENV", "local")
    config_type = {
        "dev": DevelopmentConfig(),
        "local": LocalConfig(),
        "prod": ProductionConfig(),
    }
    return config_type[env]


config: Config = get_config()