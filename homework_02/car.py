"""
создайте класс `Car`, наследник `Vehicle`
"""
from base import Vehicle
from engine import Engine


class Car(Vehicle):
    """
    Describes car entity.
    """
    def __init__(self, *args):
        super().__init__(*args)
        self._engine = None

    def __repr__(self):
        parent_repr = super().__repr__()
        return f'{parent_repr[:-1]}, engine = {self._engine})'

    @property
    def engine(self):
        return self._engine

    def set_engine(self, engine):
        if isinstance(engine, Engine):
            self._engine = engine
        else:
            raise ValueError


if __name__ == '__main__':
    c = Car(100, 20, 30)
    eng = Engine(2000)
    c.set_engine(eng)
    print(c)
