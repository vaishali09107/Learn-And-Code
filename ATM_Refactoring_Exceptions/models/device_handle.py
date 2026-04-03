class DeviceHandle:

    INVALID_DEVICE_ID = -1

    def __init__(self, device_id: int, device_name: str) -> None:
        self._device_id = device_id
        self._device_name = device_name

    @property
    def device_id(self) -> int:
        return self._device_id

    @property
    def device_name(self) -> str:
        return self._device_name

    @property
    def is_valid(self) -> bool:
        return self._device_id != self.INVALID_DEVICE_ID

    @classmethod
    def create_invalid(cls, device_name: str) -> "DeviceHandle":
        return cls(device_id=cls.INVALID_DEVICE_ID, device_name=device_name)

    def __repr__(self) -> str:
        status = "valid" if self.is_valid else "INVALID"
        return f"DeviceHandle(id={self._device_id}, name='{self._device_name}', {status})"
