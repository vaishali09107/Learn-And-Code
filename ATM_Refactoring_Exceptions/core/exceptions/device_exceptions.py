class InvalidDeviceException(Exception):

    def __init__(self, device_name: str) -> None:
        self.device_name = device_name
        super().__init__(
            f"Device '{device_name}' returned an invalid handle. "
            f"The device may be offline or unregistered."
        )


class DeviceLockedException(Exception):

    def __init__(self, device_name: str) -> None:
        self.device_name = device_name
        super().__init__(
            f"Device '{device_name}' is currently suspended. "
            f"Please contact bank support."
        )
