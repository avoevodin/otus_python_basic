from .database import db
from sqlalchemy import Column, Integer, String, Boolean


class Service(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(80), unique=True, nullable=False)
    description = Column(String(256), nullable=True)
    image = Column(String(256), nullable=True)
    free_car_wash = Column(Boolean, nullable=True, default=False)

    def __repr__(self):
        return f"<{self.__class__.__name__} {self.name!r}>"
