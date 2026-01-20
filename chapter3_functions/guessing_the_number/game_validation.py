MIN_VALID_GUESS = 1
MAX_VALID_GUESS = 100

def is_guess_valid(user_input):
    """ Checks if the user input is a valid guess """
    is_digit = user_input.isdigit()
    
    if not is_digit:
        return False
    
    is_within_range = MIN_VALID_GUESS <= int(user_input) <= MAX_VALID_GUESS
    return is_within_range
