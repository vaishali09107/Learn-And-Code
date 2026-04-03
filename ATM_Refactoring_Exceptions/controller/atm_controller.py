from core.exceptions.device_exceptions import (
    InvalidDeviceException,
    DeviceLockedException,
)
from core.exceptions.transaction_exceptions import (
    InsufficientFundsException,
    NetworkConnectionException,
)
from models.device_handle import DeviceHandle
from models.device_record import DeviceRecord
from services.device_service import DeviceService
from services.account_service import AccountService


class ATMController:

    def __init__(
        self,
        device_handle: DeviceHandle,
        device_record: DeviceRecord,
        device_service: DeviceService,
        account_service: AccountService,
    ) -> None:
        self._device_handle = device_handle
        self._device_record = device_record
        self._device_service = device_service
        self._account_service = account_service

    def withdraw(self, account_identifier: str, withdrawal_amount: float) -> None:
        try:
            self._execute_withdrawal(account_identifier, withdrawal_amount)
            print(f"Transaction completed successfully for account '{account_identifier}'.")

        except InvalidDeviceException as error:
            print(f"Device Error: {error}")

        except DeviceLockedException as error:
            print(f"Device Locked: {error}")

        except NetworkConnectionException as error:
            print(f"Network Error: {error}")

        except InsufficientFundsException as error:
            print(f"Funds Error: {error}")

    def _execute_withdrawal(
        self, account_identifier: str, withdrawal_amount: float
    ) -> None:
        self._device_service.validate_device_handle(self._device_handle)
        self._device_service.validate_device_status(self._device_record)
        self._device_service.validate_network_connection(self._device_record)
        self._account_service.validate_sufficient_balance(
            account_identifier, withdrawal_amount
        )
        self._account_service.dispense_cash(self._device_handle, withdrawal_amount)
