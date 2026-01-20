from order_services import PaymentGateway, StockService, AlertService
from order_repositories import OrderStorage

PAID_STATUS = "PAID"
CANCELLED_STATUS = "CANCELLED"
SUCCESS_STATUS = "SUCCESS"
FAILED_STATUS = "FAILED"
MINIMUM_AMOUNT = 0

class OrderHandler:
    """ Order handler """

    def __init__(self):
        """ Initializes the order handler """
        self.payment_gateway = PaymentGateway()
        self.stock_service = StockService()
        self.alert_service = AlertService()
        self.order_storage = OrderStorage()

    async def submit_order(self, order):
        """ Submits the order """
        self._verify_order(order)

        if not await self.stock_service.verify_availability(order["items"]):
            return self._create_failure_response("Insufficient inventory")

        await self.stock_service.hold_items(order["items"])

        try:
            payment_result = await self._execute_payment(order)

            if payment_result["success"]:
                await self._complete_order(order, payment_result["transaction_id"])
                return self._create_success_response(payment_result["transaction_id"])

            await self.stock_service.cancel_reservation(order["items"])
            return self._create_failure_response("Payment failed")

        except Exception:
            await self.stock_service.cancel_reservation(order["items"])
            raise

    async def revoke_order(self, order_id):
        """ Revokes the order """
        order = await self.order_storage.fetch_order_by_id(order_id)

        if order["status"] == PAID_STATUS:
            await self.payment_gateway.revert_payment(order["transaction_id"])
            await self.stock_service.replenish_inventory(order["items"])

        order["status"] = CANCELLED_STATUS
        await self.order_storage.store_order(order)

    def _verify_order(self, order):
        """ Verifies the order """
        is_order_missing = not order
        is_items_missing = not order.get("items")
        is_amount_invalid = order.get("total_amount", MINIMUM_AMOUNT) <= MINIMUM_AMOUNT
        if is_order_missing or is_items_missing or is_amount_invalid:
            raise ValueError("Invalid order")

    async def _execute_payment(self, order):
        """ Executes the payment """
        return await self.payment_gateway.execute_payment(
            order["customer_id"],
            order["total_amount"],
            order["payment_method"]
        )

    async def _complete_order(self, order, transaction_id):
        """ Completes the order """
        await self.stock_service.confirm_reservation(order["items"])
        await self.alert_service.dispatch_order_confirmation(order)
        order["transaction_id"] = transaction_id

    def _create_success_response(self, transaction_id):
        """ Creates the success response """
        return {"status": SUCCESS_STATUS, "transaction_id": transaction_id}

    def _create_failure_response(self, message):
        """ Creates the failure response """
        return {"status": FAILED_STATUS, "message": message}
