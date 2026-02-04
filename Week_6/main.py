from domain.customer import Customer
from domain.wallet import Wallet
from services.paperboy import Paperboy

def main() -> None:
    """Main function to demonstrate Law of Demeter–compliant payment collection."""
    wallet = Wallet(balance=20.0)
    customer = Customer(first_name="John", last_name="Doe", wallet=wallet)
    paperboy = Paperboy()

    amount_due = 15.0
    payment_successful = paperboy.collect_payment(customer, amount_due)

    if payment_successful:
        print("Payment collected successfully.")
        print(f"Remaining balance in wallet: {wallet.balance}")
    else:
        print("Customer could not pay. Come back later.")
        print(f"Current balance in wallet: {wallet.balance}")

if __name__ == "__main__":
    main()
