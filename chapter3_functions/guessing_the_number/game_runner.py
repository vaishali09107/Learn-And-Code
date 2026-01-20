import random
from game_input_handler import prompt_initial_guess, prompt_retry_guess
from game_validation import is_guess_valid
from gaming_rules import is_guess_below_target, is_guess_above_target, is_guess_matching
from game_display import display_too_low_hint, display_too_high_hint, display_victory_message

MIN_RANDOM_NUMBER = 1
MAX_RANDOM_NUMBER = 100
INITIAL_GUESS_COUNT = 0

def fetch_valid_guess():
    """Fetches a valid guess from the user."""
    user_input = prompt_initial_guess()

    while not is_guess_valid(user_input):
        user_input = prompt_retry_guess()

    return int(user_input)

def display_hint(guess, target_number):
    """Displays a hint based on the guess."""
    if is_guess_below_target(guess, target_number):
        display_too_low_hint()
        
    elif is_guess_above_target(guess, target_number):
        display_too_high_hint()

def run_guessing_game():
    """Runs the number guessing game."""
    target_number = random.randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    guess_count = INITIAL_GUESS_COUNT

    while True:
        current_guess = fetch_valid_guess()
        guess_count += 1

        if is_guess_matching(current_guess, target_number):
            display_victory_message(guess_count)
            break

        display_hint(current_guess, target_number)

if __name__ == "__main__":
    run_guessing_game()
