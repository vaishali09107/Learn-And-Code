class VehicleError(Exception):
    pass


class InvalidPriceError(VehicleError):
    
    def __init__(self, price: float, min_price: float, max_price: float) -> None:
        self.price = price
        self.min_price = min_price
        self.max_price = max_price
        super().__init__(
            f"Invalid price: ${price:,.2f}. "
            f"Price must be between ${min_price:,.2f} and ${max_price:,.2f}."
        )


class InvalidFuelLevelError(VehicleError):

    def __init__(self, fuel_level: float, min_level: float, max_level: float) -> None:
        self.fuel_level = fuel_level
        self.min_level = min_level
        self.max_level = max_level
        super().__init__(
            f"Invalid fuel level: {fuel_level}%. "
            f"Fuel level must be between {min_level}% and {max_level}%."
        )


class InvalidBatteryLevelError(VehicleError):

    def __init__(self, battery_level: float, min_level: float, max_level: float) -> None:
        self.battery_level = battery_level
        self.min_level = min_level
        self.max_level = max_level
        super().__init__(
            f"Invalid battery level: {battery_level}%. "
            f"Battery level must be between {min_level}% and {max_level}%."
        )


class VehicleNotFoundError(VehicleError):

    def __init__(self, vehicle_description: str) -> None:
        self.vehicle_description = vehicle_description
        super().__init__(f"Vehicle not found: {vehicle_description}")
