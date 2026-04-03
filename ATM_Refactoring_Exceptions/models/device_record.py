from enum import Enum


class DeviceStatus(Enum):
    ACTIVE = "active"
    SUSPENDED = "suspended"


class WifiStatus(Enum):
    CONNECTED = "connected"
    DISCONNECTED = "disconnected"


class DeviceRecord:

    def __init__(
        self, device_name: str, device_status: DeviceStatus, wifi_status: WifiStatus
    ) -> None:
        self._device_name = device_name
        self._device_status = device_status
        self._wifi_status = wifi_status

    @property
    def device_name(self) -> str:
        return self._device_name

    @property
    def device_status(self) -> DeviceStatus:
        return self._device_status

    @property
    def wifi_status(self) -> WifiStatus:
        return self._wifi_status

    @property
    def is_suspended(self) -> bool:
        return self._device_status == DeviceStatus.SUSPENDED

    @property
    def is_network_available(self) -> bool:
        return self._wifi_status == WifiStatus.CONNECTED

    def __repr__(self) -> str:
        return (
            f"DeviceRecord(name='{self._device_name}', "
            f"status={self._device_status.value}, "
            f"wifi={self._wifi_status.value})"
        )
