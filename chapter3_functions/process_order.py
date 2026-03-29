from order_display import display_order_error, display_order_success, log_order_saved

DISCOUNT_RATE = 0.10  
TAX_RATE = 0.18
MINIMUM_VALID_ORDER_ID = 0


def compute_discount(order_amount):
    """ Computes the discount """
    return order_amount * DISCOUNT_RATE


def compute_tax(order_amount):
    """ Computes the tax """
    return order_amount * TAX_RATE


def compute_total_amount(order_amount, discount_calculator=None, tax_calculator=None):
    """ Computes the total amount with extensible calculators """
    if discount_calculator is None:
        discount_calculator = compute_discount
    if tax_calculator is None:
        tax_calculator = compute_tax
    
    discount = discount_calculator(order_amount)
    tax = tax_calculator(order_amount)
    return (order_amount + tax) - discount


def is_invalid_order(order_id):
    """ Checks if order is invalid """
    return order_id <= MINIMUM_VALID_ORDER_ID


def submit_order(order_id, order_amount, discount_calculator=None, tax_calculator=None):
    """ Submits the order """
    if is_invalid_order(order_id):
        display_order_error()
        return

    final_amount = compute_total_amount(order_amount, discount_calculator, tax_calculator)
    log_order_saved()
    display_order_success()
    return final_amount

