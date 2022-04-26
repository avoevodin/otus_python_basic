"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):
    """
    Describes a plane entity.
    """
    def __init__(self, weight=1500, fuel=60,
                 fuel_consumption=5, max_cargo=1500):
        # TODO is it correct?
        super().__init__(weight, fuel, fuel_consumption)
        self._cargo = 0
        self._max_cargo = super().get_float_value(max_cargo)

    def __repr__(self):
        parent_repr = super().__repr__()
        return f'{parent_repr[:-1]}, cargo = {self._cargo}, max_cargo = {self.max_cargo})'

    @property
    def cargo(self):
        return self._cargo

    @cargo.setter
    def cargo(self, value):
        self._cargo = self.get_float_value(value)

    @property
    def max_cargo(self):
        return self._max_cargo

    def load_cargo(self, value):
        float_value = super().get_float_value(value)
        new_cargo = float_value + self._cargo
        if new_cargo <= self._max_cargo:
            self._cargo += float_value
        else:
            raise CargoOverload(new_cargo, self.max_cargo)

    def remove_all_cargo(self):
        old_cargo = self._cargo
        self._cargo = 0
        return old_cargo


if __name__ == '__main__':
    p = Plane(max_cargo=1500)
    p.load_cargo(500)
    p.load_cargo(100)
    print(p)
    tmp_cargo = p.remove_all_cargo()
    print(tmp_cargo)

