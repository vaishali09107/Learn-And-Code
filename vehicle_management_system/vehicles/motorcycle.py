from .fuel_vehicle import FuelVehicle


class Motorcycle(FuelVehicle):

    def __init__(self, make: str, model: str, year: int, price: float,
                 fuel_level: float = 0.0, has_sidecar: bool = False) -> None:
        super().__init__(make, model, year, price, fuel_level)
        self._has_sidecar = has_sidecar

    @property
    def has_sidecar(self) -> bool:
        return self._has_sidecar

    def display_info(self) -> None:
        sidecar_status = "Yes" if self._has_sidecar else "No"
        print(
            f"Motorcycle: {self._year} {self._make} {self._model}, "
            f"Sidecar: {sidecar_status}, "
            f"Price: ${self._price:,.2f}, "
            f"Fuel: {self._fuel_level}%"
        )
