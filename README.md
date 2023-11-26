
# The Master Mind Messages game
(https://master-mind-messages-a1f168f8791a.herokuapp.com/)

The Master Mind Messages (MMM) game is an exciting game that entices you to reveal the secrets of wisdom! Your task is to decipher the hidden code and unveil the treasure of words of wisdom that lie beyond. Drawing inspiration from the classic mastermind game, where you have to guess your opponent's colors in the correct sequence, Master Mind Messages goes beyond mere guessing. It challenges your intelligence and intuition to unlock the door to enlightenment.

The Master Mind Messages app invites you to play, ponder to reach wisdom. Are you ready to embrace the challenge and reveal the profound messages that are hidden? The journey begins now!
![image](https://github.com/CharlottaG/Secret-message-mastermind/assets/138576943/f377821e-03b2-4548-aabd-6df7c1c8cfab)


## Purpose 
The MMM game is an app for pure entertainment and pastime, an app that tickles your logical thinking and can help you relax for a while, disconnecting from the demands of everyday life. The app is intended to provide more than just the joy of solving the code; you should also take away a wise word along the way.

## User demographic
The intended audience comprises individuals with a logical mindset seeking to engage in a bit of brain exercise.

## How to use the app
When you begin the game, you'll get some instructions to follow. Your goal is to figure out a secret code that reveals words of wisdom. You have 10 chances to get it right. To play, enter a 4-digit code with different numbers (no repeats), and each number should be between 1 and 6. Before making your first guess, you'll be asked for a username to welcome you to the game. 

## Features and functions
The MMM app handles game-related tasks and user interactions, not database operations like Create, Read, Update, and Delete (CRUD). However, it does create a new random code for each game and retrieves a message from a spreadsheet when the user solves the code. The code also handles reading and displaying instructions, the user's name, and their input, which is validated and checked for a match against the random code. It also read the user’s answer whether to end the game or start a new one. The code updates the number of guesses, decreasing the remaining trials after each guess. When starting a new game, it resets the guesses and the list of previous user inputs, allowing the game to restart.

**Variables:**
   - `username`: Represents the name of the user playing the game.
   - `MAX_GUESSES`: Represents the maximum number of guesses allowed.
   - `user_input`: Represents the 4-digit code entered by the user.
   - `previous_user_input`: A list to store the user's previous guesses.
   - `random_code`: Represents the randomly generated 4-digit code for the player to guess.
   - `random_secret_message`: Represents the words of wisdom retrieved from a spreadsheet.

**Functions/Methods:**
   - `instructions()`: Prints instructions for the game.
   - `get_username()`: Asks the user for their name.
   - `set_random_code()`: Generates a random 4-digit code.
   - `get_user_input()`: Asks the user to input a 4-digit code.
   - `validate_user_input(user_input)`: Validates the user's input for 4 digits, no other characters, and that the entry is not an empty string as well as:
     - `has_duplication(code)`: Checks if there are duplicate digits in the input.
     - `digits_within_range(user_input)`: Validates that the digits are within the range 1-6.
   - `check_guess()`: Checks if the user's input matches the random code.
   - `are_digits_in_code()`: Checks if each digit in the user's input exists and is in the correct position.
   - `get_random_secret_message()`: Retrieves a random secret message from a spreadsheet.
   - `increment_guess()`: Decreases the number of guesses left.
   - `is_game_over()`: Checks if the game is over and asks the user if they want to play again.
   - `main()`: The main function that orchestrates the game flow.

**External Libraries:**
   - The app utilizes the `gspread` library to interact with Google Sheets to retrieve the wisdom words.
   - The app uses the `random` module to generate random values for the random code that user is trying to figure out.
   - 
## Error handling
The user input with the guessed code is validated for:
  - not beeing empty
  - 4 digits, not less nor more
  - no repetition of digits
  - no other characters
  - digits between 1 and 6
  - and that the entered numbers are not the same as any previous entry

## Testing
### Solved bugs
*Incrementing invalid input* – when an invalid input was made it triggered the game to increment the trials. This was fixed by changing where to call the increment function. Before it was called xxx and now it is called xxx.
*Game over after last try even if it was correct answer * - the game called the function to check if game was over before it called the function to check for the correct answer, by changing this the issue was solved.

### PEP8 validation
The code has been validated using the PEP8 validation installed in the IDE and has passed with no error or warning messages.

## Heroku deployment

 
When validation is completed the user input will be checked against the randomly genereted 4 digit code to see if there is a match, if not each digit in the user input will be checked to see if it exits in the random code, if it does it will also be checked to see if it is in the same position as in the random code. All these will be feeded back to the user to be able to have another stab at solving the code. The user have 10 trials before the game ends and they will be asked oif they want to play again.

When the user solves the code, they will be rewarded with a word of wisdom. These words of wisdoms are randomly generated from a google sheet with 60 messages.



## Future features/enhancements
Further enhancements to the Master Mind Messages game is to add:
- create user with login in, to keep track of scores when coming back to the game
- keep a top score board with the top 5 players
- play against another user instead of the app itself
- have different difficulity levels
- extend the range of digits to 0-9
  
## Testing


## Deployment

## Credits

## Idea


