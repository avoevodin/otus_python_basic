from os import getenv

SQLALCHEMY_DB_USER = "pgadmin"
SQLALCHEMY_DB_PWD = "passwd!"
SQLALCHEMY_DB_NAME = "crm_db"
SQLALCHEMY_DB_PORT = "5432"
SQLALCHEMY_DB_HOST = "localhost"
SQLALCHEMY_DB_SYNC_DRIVER = "psycopg2"
SQLALCHEMY_DB_ASYNC_DRIVER = "asyncpg"
SQLALCHEMY_POOL_SIZE = 50
SQLALCHEMY_MAX_OVERFLOW = 10
SQLALCHEMY_DB_URI_FSTRING = "postgresql+{driver}://{user}:{pwd}@{host}:{port}/{db_name}"


def get_db_uri(host=SQLALCHEMY_DB_HOST):
    return getenv(
        "SQLALCHEMY_DB_URI",
        SQLALCHEMY_DB_URI_FSTRING.format(
            driver=SQLALCHEMY_DB_SYNC_DRIVER,
            user=SQLALCHEMY_DB_USER,
            pwd=SQLALCHEMY_DB_PWD,
            host=host,
            port=SQLALCHEMY_DB_PORT,
            db_name=SQLALCHEMY_DB_NAME,
        ),
    )


class Config:
    DEBUG = False
    TESTING = False
    ENV = "development"
    SECRET_KEY = "some-secret-key"
    SQLALCHEMY_DATABASE_URI = get_db_uri()
    SQLALCHEMY_DB_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    DEBUG = True
    TESTING = True


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    ENV = "production"
    SECRET_KEY = "prod-secret-key"
    SQLALCHEMY_DB_HOST = "pg"
    SQLALCHEMY_DATABASE_URI = get_db_uri(SQLALCHEMY_DB_HOST)
