import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from vehicle_management_system.vehicles.car import Car
from vehicle_management_system.vehicles.motorcycle import Motorcycle
from vehicle_management_system.vehicles.electric_car import ElectricCar
from vehicle_management_system.managers.vehicle_manager import VehicleManager
from vehicle_management_system.exceptions.vehicle_exceptions import (
    InvalidPriceError,
    InvalidFuelLevelError,
)


def create_vehicles():
    honda_accord = Car(
        make="Honda",
        model="Accord",
        year=2023,
        price=28000,
        fuel_level=100,
    )

    harley_street = Motorcycle(
        make="Harley-Davidson",
        model="Street 750",
        year=2022,
        price=7500,
        fuel_level=80,
        has_sidecar=False,
    )

    tesla_model_3 = ElectricCar(
        make="Tesla",
        model="Model 3",
        year=2023,
        price=42000,
        battery_level=100,
    )

    return honda_accord, harley_street, tesla_model_3


def test_individual_vehicles(honda_accord, harley_street, tesla_model_3):
    print("Testing Vehicles:")
    honda_accord.start()
    honda_accord.display_info()
    honda_accord.stop()
    print()

    harley_street.start()
    harley_street.display_info()
    print()

    tesla_model_3.start()
    tesla_model_3.display_info()


def test_fleet_management(honda_accord, harley_street, tesla_model_3):
    manager = VehicleManager()
    manager.add_vehicle(honda_accord)
    manager.add_vehicle(harley_street)
    manager.add_vehicle(tesla_model_3)

    manager.display_all()

    total_value = manager.calculate_total_value()
    print(f"\nTotal Value: ${total_value:,.2f}")

    print("\nStarting all vehicles:")
    manager.start_all()


def test_encapsulation(honda_accord):
    print("\n=== Encapsulation Problem ===")

    try:
        honda_accord.price = -1000
    except InvalidPriceError as price_error:
        print(f"Price validation: {price_error}")

    try:
        honda_accord.fuel_level = 500
    except InvalidFuelLevelError as fuel_error:
        print(f"Fuel validation: {fuel_error}")

    print(f"Car price after invalid set: ${honda_accord.price:,.2f}")
    print(f"Car fuel after invalid set: {honda_accord.fuel_level}%")


def main():
    print("=== Vehicle Management Demo ===\n")

    honda_accord, harley_street, tesla_model_3 = create_vehicles()
    test_individual_vehicles(honda_accord, harley_street, tesla_model_3)
    test_fleet_management(honda_accord, harley_street, tesla_model_3)
    test_encapsulation(honda_accord)

    print("\n=== Demo Complete ===")


if __name__ == "__main__":
    main()
