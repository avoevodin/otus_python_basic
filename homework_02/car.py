"""
создайте класс `Car`, наследник `Vehicle`
"""
from .base import Vehicle
from .engine import Engine


class Car(Vehicle):
    """
    Describes car entity.
    """
    def __init__(self):
        super.__init__()
        self._engine = Engine()

    @property
    def engine(self):
        return self._engine

    def set_engine(self, engine):
        if isinstance(engine, Engine):
            self._engine = engine
        else:
            raise ValueError
