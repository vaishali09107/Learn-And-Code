"""Display module for game output messages."""

TOO_LOW_MESSAGE = "Too low. Guess again"
TOO_HIGH_MESSAGE = "Too high. Guess again"


def display_too_low_hint(output_func=None):
    """Displays hint when guess is too low."""
    if output_func is None:
        output_func = print
    output_func(TOO_LOW_MESSAGE)


def display_too_high_hint(output_func=None):
    """Displays hint when guess is too high."""
    if output_func is None:
        output_func = print
    output_func(TOO_HIGH_MESSAGE)


def display_victory_message(guess_count, output_func=None):
    """Displays the victory message with guess count."""
    if output_func is None:
        output_func = print
    output_func(f"You guessed it in {guess_count} guesses!")

