class InsufficientFundsException(Exception):

    def __init__(
        self, account_identifier: str, withdrawal_amount: float, current_balance: float
    ) -> None:
        self.account_identifier = account_identifier
        self.withdrawal_amount = withdrawal_amount
        self.current_balance = current_balance
        super().__init__(
            f"Account '{account_identifier}' has insufficient funds. "
            f"Requested: ${withdrawal_amount:.2f}, Available: ${current_balance:.2f}."
        )


class NetworkConnectionException(Exception):

    def __init__(self, device_name: str) -> None:
        self.device_name = device_name
        super().__init__(
            f"Device '{device_name}' has no active network connection. "
            f"Transaction cannot proceed."
        )
