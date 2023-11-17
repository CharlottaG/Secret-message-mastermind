import random


def instructions():
    """Print instructions to user on how to play the game."""
    print("Can you find the code guarding the secret message?")
    print("It is a 4 digit code with numbers between 1 and 6.")
    print("There can be no duplications.\n")
    print("You have 10 tries before the message will self-destruct.\n")
    print("   ! indicates one correct number, placed correct.\n")
    print("   * indicates one correct number, placed wrong.\n")
    print("Good Luck and Hurry Up!\n")
    print("__________________________________________________\n")


def get_username():
    """Asks user for username, validates user input"""
    while True:
        username = input("Please enter your name: \n").strip()
        if username != "":
            print(f"\nAha {username}! Curious about the secret message?\n")
            break
        else:
            print("You can't keep it a secret! Please enter your name:")


def guess():
    """Asks user to enter 4 digits"""
    """validates for numbers and no duplication."""
    global user_input

    while True:
        user_input = input("Please enter a 4 digit code: \n")
        # Validates for not being empty
        if user_input == "":
            print("No, no, no! You can't leave this empty!\n")
        # Validates digits and no other characters
        elif not user_input.isdigit():
            print("No, no, no! Digits only!\n")
        # Validates 4 digits
        elif len(user_input) != 4:
            print("No, no, no! 4 digits please!\n")
        # Validates duplication
        elif has_duplication(user_input) is True:
            print("No, no, no! No duplications!\n")
        # Prints guess and increments number for each new guess
        else:
            increment_guess()
            print(f"Guess {current_guess}: {user_input}\n")
            #check_for_match()
            break


def has_duplication(code):
    """Checks for duplication in code"""
    entered_numbers = set()
    for digit in code:
        if digit in entered_numbers:
            return True
        entered_numbers.add(digit)
    return False


def increment_guess():
    """ Increments with 1 to track the number of guesses for each new entry """
    global current_guess
    current_guess += 1

current_guess = 0


def set_random_code():
    """ Create random 4 digit code with no duplications """
    global random_code
    #random_code = random.sample("123456", 4)
    random_code = 6543


#def check_for_match():
    """ Checks if user input matches random code """
    if user_input == random_code:
        print("The secret message is: Carpe diem!\n")
    else:
        guess()


def main():
   # instructions()
   get_username()
   # set_random_code()
   guess()


main()
