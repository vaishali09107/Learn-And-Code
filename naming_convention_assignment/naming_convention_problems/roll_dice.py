import random

def roll_dice(number_of_sides):
    roll_result=random.randint(1, number_of_sides)
    return roll_result

def dice_rolling_game():
    number_of_sides=6
    keep_rolling=True
    while keep_rolling:
        user_input=input("Ready to roll? Enter Q to Quit :\n")
        if user_input.lower() !="q":
            roll_result=roll_dice(number_of_sides)
            print("You have rolled a",roll_result)
        else:
            keep_rolling=False
            
dice_rolling_game()