from core.exceptions.transaction_exceptions import InsufficientFundsException
from models.device_handle import DeviceHandle

_SIMULATED_ACCOUNT_BALANCES: dict[str, float] = {
    "ACC-1001": 5000.00,
    "ACC-1002": 200.00,
    "ACC-1003": 0.00,
}


class AccountService:

    @staticmethod
    def validate_sufficient_balance(
        account_identifier: str, withdrawal_amount: float
    ) -> None:
        current_balance = _SIMULATED_ACCOUNT_BALANCES.get(account_identifier, 0.00)

        if current_balance < withdrawal_amount:
            raise InsufficientFundsException(
                account_identifier, withdrawal_amount, current_balance
            )

    @staticmethod
    def dispense_cash(device_handle: DeviceHandle, withdrawal_amount: float) -> None:
        print(f"Dispensing ${withdrawal_amount:.2f} from {device_handle.device_name}. Please collect your cash.")
