import random

def is_valid_guess(s):
    if s.isdigit() and 1<= int(s) <=100:
        return True
    else:
        return False

def number_guessing_game():
    secret_number=random.randint(1,100)
    guessed_correctly=False
    user_guess=input("Guess a number between 1 and 100:")
    number_of_guesses=0
    while not guessed_correctly:
        if not is_valid_guess(user_guess):
            user_guess=input("I wont count this one Please enter a number between 1 to 100")
            continue
        else:
            number_of_guesses+=1
            user_guess=int(user_guess)
        if user_guess<secret_number:
            user_guess=input("Too low. Guess again\n")
        elif user_guess>secret_number:
            user_guess=input("Too High. Guess again\n")
        else:
            print("You guessed it in",number_of_guesses,"guesses!")
            guessed_correctly=True

number_guessing_game()
