from abc import ABC
from .vehicle import Vehicle
from ..utils.validators import validate_fuel_level


class FuelVehicle(Vehicle, ABC):

    def __init__(self, make: str, model: str, year: int, price: float,
                 fuel_level: float = 0.0) -> None:
        super().__init__(make, model, year, price)
        self._fuel_level = validate_fuel_level(fuel_level)

    @property
    def fuel_level(self) -> float:
        return self._fuel_level

    @fuel_level.setter
    def fuel_level(self, new_fuel_level: float) -> None:
        self._fuel_level = validate_fuel_level(new_fuel_level)

    def refuel(self, amount: float) -> None:
        updated_fuel_level = self._fuel_level + amount
        self._fuel_level = validate_fuel_level(updated_fuel_level)
        print(f"Refueled {self._make} {self._model}. Fuel level: {self._fuel_level}%")

    def start(self) -> None:
        if self._fuel_level > 0:
            self._is_running = True
            print(f"{self._make} {self._model} engine started.")
        else:
            print(f"Cannot start {self._make} {self._model} — no fuel!")
