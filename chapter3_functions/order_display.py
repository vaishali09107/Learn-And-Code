"""Display module for order processing output messages."""

ORDER_ERROR_MESSAGE = "Order cannot be empty"
ORDER_SUCCESS_MESSAGE = "Order placed successfully"
ORDER_SAVED_MESSAGE = "Order saved in database"


def display_order_error(output_func=None):
    """Displays the error message for invalid order."""
    if output_func is None:
        output_func = print
    output_func(ORDER_ERROR_MESSAGE)


def display_order_success(output_func=None):
    """Displays the success message for order placement."""
    if output_func is None:
        output_func = print
    output_func(ORDER_SUCCESS_MESSAGE)


def log_order_saved(output_func=None):
    """Logs that the order was saved to database."""
    if output_func is None:
        output_func = print
    output_func(ORDER_SAVED_MESSAGE)

