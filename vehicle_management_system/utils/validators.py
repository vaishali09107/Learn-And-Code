from ..exceptions.vehicle_exceptions import (
    InvalidPriceError,
    InvalidFuelLevelError,
    InvalidBatteryLevelError,
)

MIN_PRICE: float = 0.0
MAX_PRICE: float = 1_000_000.0

MIN_FUEL_LEVEL: float = 0.0
MAX_FUEL_LEVEL: float = 100.0

MIN_BATTERY_LEVEL: float = 0.0
MAX_BATTERY_LEVEL: float = 100.0


def validate_price(price: float) -> float:
    if not MIN_PRICE <= price <= MAX_PRICE:
        raise InvalidPriceError(price, MIN_PRICE, MAX_PRICE)
    return price


def validate_fuel_level(fuel_level: float) -> float:
    if not MIN_FUEL_LEVEL <= fuel_level <= MAX_FUEL_LEVEL:
        raise InvalidFuelLevelError(fuel_level, MIN_FUEL_LEVEL, MAX_FUEL_LEVEL)
    return fuel_level


def validate_battery_level(battery_level: float) -> float:
    if not MIN_BATTERY_LEVEL <= battery_level <= MAX_BATTERY_LEVEL:
        raise InvalidBatteryLevelError(
            battery_level, MIN_BATTERY_LEVEL, MAX_BATTERY_LEVEL
        )
    return battery_level
