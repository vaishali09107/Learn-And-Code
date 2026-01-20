DISCOUNT_RATE = 0.10  
TAX_RATE = 0.18
MINIMUM_VALID_ORDER_ID = 0

def submit_order(order_id, order_amount):
    """ Submits the order """
    if is_invalid_order(order_id):
        display_error_message()
        return

    final_amount = compute_total_amount(order_amount)
    store_order(order_id, final_amount)
    display_success_message()

def compute_total_amount(order_amount):
    """ Computes the total amount """
    discount = compute_discount(order_amount)
    tax = compute_tax(order_amount)
    return (order_amount + tax) - discount

def compute_discount(order_amount):
    """ Computes the discount """
    return order_amount * DISCOUNT_RATE

def compute_tax(order_amount):
    """ Computes the tax """
    return order_amount * TAX_RATE

def is_invalid_order(order_id):
    """ Checks if order is invalid """
    return order_id <= MINIMUM_VALID_ORDER_ID

def display_error_message():
    """ Displays the error message """
    print("Order cannot be empty")

def display_success_message():
    """ Displays the success message """
    print("Order placed successfully")

def store_order(order_id, amount):
    """ Stores the order """
    print("Order saved in database")
