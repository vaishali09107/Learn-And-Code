from domain.customer import Customer

class Paperboy:
    """Service object responsible for collecting payments from customers."""

    def collect_payment(self, customer: Customer, payment_amount: float) -> bool:
        return customer.pay(payment_amount)


