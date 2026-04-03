from core.exceptions.device_exceptions import (
    InvalidDeviceException,
    DeviceLockedException,
)
from core.exceptions.transaction_exceptions import NetworkConnectionException
from models.device_handle import DeviceHandle
from models.device_record import DeviceRecord


class DeviceService:

    @staticmethod
    def validate_device_handle(device_handle: DeviceHandle) -> None:
        if not device_handle.is_valid:
            raise InvalidDeviceException(device_handle.device_name)

    @staticmethod
    def validate_device_status(device_record: DeviceRecord) -> None:
        if device_record.is_suspended:
            raise DeviceLockedException(device_record.device_name)

    @staticmethod
    def validate_network_connection(device_record: DeviceRecord) -> None:
        if not device_record.is_network_available:
            raise NetworkConnectionException(device_record.device_name)
