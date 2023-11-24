import random
#import gspread
#from google.oauth2.service_account import Credentials

random_code = ""
user_input = ""
previous_user_input = []
MAX_GUESSES = 3


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
    global username

    while True:
        username = input("Please enter your name: \n").strip()
        if username != "":
            print(f"\nAha {username.upper()}! Curious about the secret message?\n")
            break
        else:
            print("You can't keep it a secret! Please enter your name:")


def set_random_code():
    """ Create random 4 digit code with no duplications """
    global random_code
    random_code = "".join(random.sample("123456", 4))


def get_user_input():
    """ Asks user to enter a 4 digit code and validates the input """
    global user_input

    while True:
        user_input = input("Please enter a 4 digit code: ")
        if validate_user_input(user_input):
            return user_input
        else:
            print("Please try again!\n")


def validate_user_input(user_input):
    """ Validates user input """
    # Validates that input is not empty
    if user_input == "":
        print("No, no, no! You can't leave this empty!\n")
    # Validates input is digits and no other characters
    elif not user_input.isdigit():
        print("No, no, no! Digits only!\n")
    # Validates input is 4 digits
    elif len(user_input) != 4:
        print("No, no, no! 4 digits please!\n")
    # Validates input for unique digits, no duplicate digits allowed
    elif has_duplication(user_input) is True:
        print("No, no, no! No duplications!\n")
    # Validates user input is not the same as any previous input
    elif user_input in set(previous_user_input):
        print("No, no, no! You have already tried this code.\n")
    else:
        previous_user_input.append(user_input)
        increment_guess()
        check_guess()


def has_duplication(code):
    """Checks for duplication in code"""
    entered_numbers = set()
    for digit in code:
        if digit in entered_numbers:
            return True
        entered_numbers.add(digit)
    return False


def check_guess():
    """
    Check if user input match random code.
    """

    global user_input
    global random_code

    print(f"User: {user_input}, Code:{random_code}")

    if user_input == random_code:
        print("Congratulations, you guess the code! The secret message is: Carpe diem!\n")
        is_game_over()
    else:
        are_digits_in_code()


def are_digits_in_code():
    """ Check if each digit in user input exits and match random code """
    global user_input
    global random_code

    user_input_array = [int(x) for x in str(user_input)]
    random_code_array = [int(x) for x in str(random_code)]

    #Iterate through index and value in user input
    for user_index, user_digit in enumerate(user_input_array):
        # Check if digit exits in random code
        if user_digit in random_code_array:
            # Check if digit is in the same position as in random code
            if user_digit == random_code_array[user_index]:
                print(f"Number {user_digit} is placed correct.")
            # Digit exits in random code, but in another position
            else: 
                print(f"Number {user_digit} is placed incorrect. ")
            # Move to check the next digit in user input
            continue
        else:
            print(f"Number {user_digit} is not in the code")


def increment_guess(): 
    """ Increments guess for each new entry"""
    global MAX_GUESSES
    
    if MAX_GUESSES > 0:
        MAX_GUESSES -= 1
        print(f"Number of guesses left: {MAX_GUESSES}\n")
    if MAX_GUESSES == 0:
        print(" You are out of guesses!")
        is_game_over()

            
def is_game_over():
    """ Check if player wants to play new game and resets all values """
    answer = input("Do you want to play again? Y/N\n")
    global current_guess
    global guesses_left

    if answer.upper() == "Y":
        """ Reset values for new game"""
        del previous_user_input[:]
        current_guess = 0
        guesses_left = 3
        print(f"So you are still curious! Let's go {username}\n")
        set_random_code()
        guess_code()
    if answer.upper() == "N":
        exit()
    else:
        print("No, no, no! /ou need to enter Y or N.\n")
        is_game_over()


def main():
    instructions()
    get_username()
    set_random_code()
    get_user_input()
    

main()
