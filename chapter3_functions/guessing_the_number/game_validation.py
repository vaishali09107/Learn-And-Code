MIN_VALID_GUESS = 1
MAX_VALID_GUESS = 100

def is_guess_valid(user_input):
    """ Checks if the user input is a valid guess """
    return user_input.isdigit() and MIN_VALID_GUESS <= int(user_input) <= MAX_VALID_GUESS
