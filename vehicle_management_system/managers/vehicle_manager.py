from typing import List

from ..vehicles.vehicle import Vehicle


class VehicleManager:
    
    def __init__(self) -> None:
        self._vehicles: List[Vehicle] = []

    @property
    def vehicle_count(self) -> int:
        return len(self._vehicles)

    def add_vehicle(self, vehicle: Vehicle) -> None:
        if not isinstance(vehicle, Vehicle):
            raise TypeError(
                f"Expected a Vehicle instance, got {type(vehicle).__name__}"
            )
        self._vehicles.append(vehicle)
        print(f"{type(vehicle).__name__} added: {vehicle}")

    def display_all(self) -> None:
        print("\n=== All Vehicles ===")
        if not self._vehicles:
            print("No vehicles in the fleet.")
            return

        for vehicle in self._vehicles:
            vehicle.display_info()

    def calculate_total_value(self) -> float:
        total_value = sum(vehicle.price for vehicle in self._vehicles)
        return total_value

    def start_all(self) -> None:
        print("\nStarting all vehicles:")
        for vehicle in self._vehicles:
            vehicle.start()

    def stop_all(self) -> None:
        print("\nStopping all vehicles:")
        for vehicle in self._vehicles:
            vehicle.stop()
