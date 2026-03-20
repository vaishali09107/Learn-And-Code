from .fuel_vehicle import FuelVehicle


class Car(FuelVehicle):
    def display_info(self) -> None:
        print(
            f"Car: {self._year} {self._make} {self._model}, "
            f"Price: ${self._price:,.2f}, "
            f"Fuel: {self._fuel_level}%"
        )
