from abc import ABC

from .vehicle import Vehicle
from ..utils.validators import validate_battery_level


class ElectricVehicle(Vehicle, ABC):
    
    def __init__(self, make: str, model: str, year: int, price: float,
                 battery_level: float = 0.0) -> None:
        super().__init__(make, model, year, price)
        self._battery_level = validate_battery_level(battery_level)

    @property
    def battery_level(self) -> float:
        return self._battery_level

    @battery_level.setter
    def battery_level(self, new_battery_level: float) -> None:
        self._battery_level = validate_battery_level(new_battery_level)

    def charge(self, amount: float) -> None:
        updated_battery_level = self._battery_level + amount
        self._battery_level = validate_battery_level(updated_battery_level)
        print(
            f"Charged {self._make} {self._model}. "
            f"Battery level: {self._battery_level}%"
        )

    def start(self) -> None:
        if self._battery_level > 0:
            self._is_running = True
            print(f"{self._make} {self._model} electric motor started.")
        else:
            print(f"Cannot start {self._make} {self._model} — battery dead!")
