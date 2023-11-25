
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

## Features


## Error handling
The user input with the guessed code is validated for:
  - not beeing empty
  - 4 digits, not less nor more
  - no repetition of digits
  - no other characters
  - digits between 1 and 6
  - and that the entered numbers are not the same as any previous entry

## Heroku deployment

 
When validation is completed the user input will be checked against the randomly genereted 4 digit code to see if there is a match, if not each digit in the user input will be checked to see if it exits in the random code, if it does it will also be checked to see if it is in the same position as in the random code. All these will be feeded back to the user to be able to have another stab at solving the code. The user have 10 trials before the game ends and they will be asked oif they want to play again.

When the user solves the code, they will be rewarded with a word of wisdom. These words of wisdoms are randomly generated from a google sheet with 60 messages.



## Future features/enhancements

## Testing

## Deployment

## Credits

## Idea


