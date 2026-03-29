class OrderStorage:
    """ Order storage """
    
    async def fetch_order_by_id(self, order_id):
        """ Fetches the order by id """
        return {
            "id": order_id,
            "status": "PAID",
            "transaction_id": "TXN123",
            "items": []
        }

    async def store_order(self, order):
        """ Stores the order """
        pass
