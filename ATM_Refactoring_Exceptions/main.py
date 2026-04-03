import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from models.device_handle import DeviceHandle
from models.device_record import DeviceRecord, DeviceStatus, WifiStatus
from services.device_service import DeviceService
from services.account_service import AccountService
from controller.atm_controller import ATMController


VALID_DEVICE_ID = 1
VALID_ACCOUNT_IDENTIFIER = "ACC-1001"
LOW_BALANCE_ACCOUNT_IDENTIFIER = "ACC-1002"
DEFAULT_DEVICE_NAME = "ATM-BRANCH-42"
STANDARD_WITHDRAWAL_AMOUNT = 500.00
OVER_LIMIT_WITHDRAWAL_AMOUNT = 10_000.00


def _build_controller(
    device_handle: DeviceHandle, device_record: DeviceRecord
) -> ATMController:
    return ATMController(
        device_handle=device_handle,
        device_record=device_record,
        device_service=DeviceService(),
        account_service=AccountService(),
    )


def run_successful_withdrawal() -> None:
    print("\nScenario 1: Successful Withdrawal")
    handle = DeviceHandle(VALID_DEVICE_ID, DEFAULT_DEVICE_NAME)
    record = DeviceRecord(
        DEFAULT_DEVICE_NAME, DeviceStatus.ACTIVE, WifiStatus.CONNECTED
    )
    controller = _build_controller(handle, record)
    controller.withdraw(VALID_ACCOUNT_IDENTIFIER, STANDARD_WITHDRAWAL_AMOUNT)


def run_invalid_device_scenario() -> None:
    print("\nScenario 2: Invalid Device Handle")
    handle = DeviceHandle.create_invalid(DEFAULT_DEVICE_NAME)
    record = DeviceRecord(
        DEFAULT_DEVICE_NAME, DeviceStatus.ACTIVE, WifiStatus.CONNECTED
    )
    controller = _build_controller(handle, record)
    controller.withdraw(VALID_ACCOUNT_IDENTIFIER, STANDARD_WITHDRAWAL_AMOUNT)


def run_device_locked_scenario() -> None:
    print("\nScenario 3: Device Locked / Suspended")
    handle = DeviceHandle(VALID_DEVICE_ID, DEFAULT_DEVICE_NAME)
    record = DeviceRecord(
        DEFAULT_DEVICE_NAME, DeviceStatus.SUSPENDED, WifiStatus.CONNECTED
    )
    controller = _build_controller(handle, record)
    controller.withdraw(VALID_ACCOUNT_IDENTIFIER, STANDARD_WITHDRAWAL_AMOUNT)


def run_network_disconnected_scenario() -> None:
    print("\nScenario 4: Network Disconnected")
    handle = DeviceHandle(VALID_DEVICE_ID, DEFAULT_DEVICE_NAME)
    record = DeviceRecord(
        DEFAULT_DEVICE_NAME, DeviceStatus.ACTIVE, WifiStatus.DISCONNECTED
    )
    controller = _build_controller(handle, record)
    controller.withdraw(VALID_ACCOUNT_IDENTIFIER, STANDARD_WITHDRAWAL_AMOUNT)


def run_insufficient_funds_scenario() -> None:
    print("\nScenario 5: Insufficient Funds")
    handle = DeviceHandle(VALID_DEVICE_ID, DEFAULT_DEVICE_NAME)
    record = DeviceRecord(
        DEFAULT_DEVICE_NAME, DeviceStatus.ACTIVE, WifiStatus.CONNECTED
    )
    controller = _build_controller(handle, record)
    controller.withdraw(LOW_BALANCE_ACCOUNT_IDENTIFIER, OVER_LIMIT_WITHDRAWAL_AMOUNT)


def main() -> None:
    run_successful_withdrawal()
    run_invalid_device_scenario()
    run_device_locked_scenario()
    run_network_disconnected_scenario()
    run_insufficient_funds_scenario()


if __name__ == "__main__":
    main()
