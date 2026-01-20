INITIAL_GUESS_PROMPT = "Guess a number between 1 and 100:"
RETRY_GUESS_PROMPT = "I won't count this one, please enter a number between 1 to 100:"


def prompt_initial_guess(input_func=None):
    """ Prompts for the first guess from the user """
    if input_func is None:
        input_func = input
    return input_func(INITIAL_GUESS_PROMPT).strip()


def prompt_retry_guess(input_func=None):
    """ Prompts for the retry guess from the user """
    if input_func is None:
        input_func = input
    return input_func(RETRY_GUESS_PROMPT).strip()


def prompt_guess(input_func=None):
    """ Prompts for a guess from the user """
    if input_func is None:
        input_func = input
    return input_func("").strip()

