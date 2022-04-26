from abc import ABC

from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    """
    The class of vehicle.
    """
    def __init__(self, weight=1500, fuel=60, fuel_consumption=5):
        super().__init__()
        self._weight = weight
        self._fuel = fuel
        self._fuel_consumption = fuel_consumption
        self._started = False

    def __repr__(self):
        return f'{self.__class__.__name__} (weight = {self._weight}, started = {self._started}, ' \
               f'fuel = {self._fuel}, fuel_consumption = {self._fuel_consumption})'

    @property
    def started(self):
        return self._started

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        self._weight = self.get_float_value(value)

    @property
    def fuel(self):
        return self._fuel

    @fuel.setter
    def fuel(self, value):
        self._fuel = self.get_float_value(value)
        print(self._fuel)

    @property
    def fuel_consumption(self):
        return self._fuel_consumption

    @fuel_consumption.setter
    def fuel_consumption(self, value):
        self._fuel_consumption = self.get_float_value(value)

    def start(self):
        """
        Set started as True if fuel is a positive number.
        """
        if self._fuel:
            self._started = True
        else:
            raise LowFuelError(self._fuel)

    def move(self, distance):
        """
        Moves vehicle for passed distance if fuel is enough.
        Decreases fuel depending on the distance travelled.
        """
        float_distance = self.get_float_value(distance)
        fuel_left = self._fuel - self._fuel_consumption * float_distance
        if fuel_left >= 0:
            self._fuel = fuel_left
        else:
            raise NotEnoughFuel(self._fuel)

    @staticmethod
    def get_float_value(value):
        float_value = float(value)
        if float_value >= 0:
            return float_value
        else:
            raise ValueError


if __name__ == '__main__':
    v = Vehicle()
    v.fuel = '100'
    print(v)
    v.start()
    v.move(1000)
    print(v)
