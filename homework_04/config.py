import os

pg_conn_format_string = "postgresql+{driver}://{user}:{pwd}@{host}:{port}/{db_name}"

PG_DRIVER = "asyncpg"
PG_SYNC_DRIVER = "pg8000"
PG_USER = "pgadmin"
PG_PWD = "passwd!"
PG_HOST = "localhost"
PG_PORT = "5432"
PG_DB_NAME = "blog"


PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or pg_conn_format_string.format(
    driver=PG_DRIVER,
    user=PG_USER,
    pwd=PG_PWD,
    host=PG_HOST,
    port=PG_PORT,
    db_name=PG_DB_NAME,
)

PG_SYNC_CONN_URI = pg_conn_format_string.format(
    driver=PG_SYNC_DRIVER,
    user=PG_USER,
    pwd=PG_PWD,
    host=PG_HOST,
    port=PG_PORT,
    db_name=PG_DB_NAME,
)

PG_DB_ECHO = True
