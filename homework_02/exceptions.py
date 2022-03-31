"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""


class LowFuelError(Exception):
    """
    Exception raises when the fuel level is low.
    """
    def __init__(self, fuel, message="The fuel level is low."):
        self.fuel = fuel
        self.message = message
        super().__init__(message)

    def __str__(self):
        return f'{self.fuel} -> {self.message}'


class NotEnoughFuel(Exception):
    """
    Exception raises when the fuel level is not enough for further moving.
    """
    def __init__(self, fuel, message="The fuel level is not enough."):
        self.fuel = fuel
        self.message = message
        super().__init__(message)

    def __str__(self):
        return f'{self.fuel} -> {self.message}'


class CargoOverload(Exception):
    """
    Exception raises when the vehicle is overloaded with cargo.
    """
    def __init__(self, cargo, max_cargo,
                 message="The vehicle is overload."):
        self.cargo = cargo
        self.max_cargo = max_cargo
        self.message = message
        super().__init__(message)

    def __str__(self):
        return f'{self.cargo} -> {self.message} Max cargo is {self.max_cargo}'
