def prompt_initial_guess():
    """ Prompts for the first guess from the user """
    return input("Guess a number between 1 and 100:").strip()

def prompt_retry_guess():
    """ Prompts for the retry guess from the user """
    return input("I won't count this one, please enter a number between 1 to 100:").strip()

def prompt_guess():
    """ Prompts for a guess from the user """
    return input().strip()
