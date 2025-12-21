import random

def is_valid_guess(user_input: str) -> bool:
    """ Returns True if the input is a number between 1 and 100. """
    if not user_input.isdigit():
        return False

    guess = int(user_input)
    return 1 <= guess <= 100

def get_valid_guess() -> int:
    """ Prompts the user until a valid guess is entered. """
    user_input = input("Guess a number between 1 and 100: ")

    while not is_valid_guess(user_input):
        user_input = input(
            "Invalid input. Please enter a number between 1 and 100: "
        )

    return int(user_input)

def compare_guess(guess: int, secret_number: int) -> str:
    """ Compares the guess with the secret number. """
    if guess < secret_number:
        return "LOW"
    if guess > secret_number:
        return "HIGH"
    return "CORRECT"

def play_number_guessing_game() -> None:
    """ Controls the game flow. """
    secret_number = random.randint(1, 100)
    guess_count = 0
        
    while True:
        guess = get_valid_guess()
        guess_count += 1

        comparison_result = compare_guess(guess, secret_number)

        if comparison_result == "LOW":
            print("Too low. Guess again.")
        elif comparison_result == "HIGH":
            print("Too high. Guess again.")
        else:
            print(f"You guessed it in {guess_count} guesses!")
            break

play_number_guessing_game()
