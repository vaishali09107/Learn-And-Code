from .electric_vehicle import ElectricVehicle


class ElectricCar(ElectricVehicle):

    def display_info(self) -> None:
        print(
            f"Electric Car: {self._year} {self._make} {self._model}, "
            f"Price: ${self._price:,.2f}, "
            f"Battery: {self._battery_level}%"
        )
