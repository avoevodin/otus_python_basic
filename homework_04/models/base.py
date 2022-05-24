from sqlalchemy import Integer, Column, create_engine
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, AsyncSession
from sqlalchemy.orm import declarative_base, declared_attr, sessionmaker

import config


class Base:
    @declared_attr
    def __tablename__(cls):
        return f"{cls.__name__.lower()}s"

    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return str(self)


async_engine: AsyncEngine = create_async_engine(
    config.PG_CONN_URI, echo=config.PG_DB_ECHO
)
Session = sessionmaker(async_engine, expire_on_commit=False, class_=AsyncSession)

sync_engine = create_engine(url=config.PG_SYNC_CONN_URI, echo=config.PG_DB_ECHO)
Base = declarative_base(bind=sync_engine, cls=Base)
