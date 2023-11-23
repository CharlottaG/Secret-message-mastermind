import random
#import gspread
#from google.oauth2.service_account import Credentials

current_guess = 0
guesses_left = 3
random_code = ""
previous_user_input = ""


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


def set_random_code():
    """ Create random 4 digit code with no duplications """
    global random_code
    random_code = "".join(random.sample("123456", 4))
    print(f"random code: {random_code}\n")


def guess_code():
    """Asks user to enter 4 digits"""
    """validates for numbers and no duplication."""
    global user_input
    global previous_user_input

    while True:
        user_input = input("Please enter a 4 digit code: \n")
        # Validates not empty
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
        # Check that the user input is not the same as the previous input
        elif user_input == previous_user_input:
            print("No, no, no! You have already tried this code\n") 
        # Check for match against random code
        else:
            previous_user_input = user_input
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
    if user_input == random_code:
        print("Congratulations, you guess the code! The secret message is: Carpe diem!\n")
    else:
        increment_guess()


def increment_guess(): 
    """ Increments guess for each new entry"""
    global current_guess
    global user_input
    global guesses_left
    
    if current_guess < 2:
        current_guess += 1
        guesses_left -= 1
        print(f"Guess {current_guess}: {user_input}\n")
        print(f"{guesses_left} guesses left!\n")
            

#""def is_game_over():
#        if guesses_left < 3:
#            guess_code()    
#        else:
#           print("Code unbroken; the secret message is forever lost!")  
        

def main():
    instructions()
    get_username()
    set_random_code()
   # is_game_over()
    guess_code()
    

main()
