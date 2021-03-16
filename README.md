# Memory Game

## Story

You're tasked with a terminal implementation of [Memory Game](https://en.wikipedia.org/wiki/Concentration_(card_game)) for a single player

## What are you going to learn?

In this project, you will improve the following skills and topic:
- using nested lists
- designing a simple game application in terminal
- using functions


## Tasks

1. Implement `generate_board(height, width)` to return a randomly generated matrix of alphabet letters (a list of lists). The inner lists are columns.
    - A list of lists is returned, representing a list of columns
    - If the amount of letters required to generate the board (based on given height and width) is greater than the amount of letters in latin alphabet, raise a `ValueError`.
    - If the amount of letters required to generate the board (based on given height and width) is odd, raise a `ValueError`.
    - The board consists of pairs of letters from latin alphabet. Example:
```
AFCH
DFED
CBAE
GBGH
```

2. The user can select a field on the board, by writing its coordinates like this: `B2`, where the letter is the column (A is 0, B is 1, and so on...) and the number is the row (don't forget that 1 actually refers to 0 index!).
    - The program checks whether user's input is in the `LETTERNUMBER` format (like `B2` or `F10`).
    - The program checks whether the inputted number is positive and does not exceed the amount of rows the board has.
    - The program checks whether the inputted letter's position in the alphabet does not exceed the amount of column the board has.
    - The program keeps asking the user for selecting a field, until receiving valid input.
    - After successful validation of the input, the selected field's coordinates are passed further into the program's logic as an integer tuple `(row, column)`

3. The user can select the difficulty level before starting the game. The difficulty level dictates the size of the board.
    - The user can pick one of the three difficulty levels - easy, medium and hard.
    - When picked the Easy difficulty level, the board's size should be `5x4`
    - When picked the Medium difficulty level, the board's size should be `5x6`
    - When picked the Hard difficulty level, the board's size should be `5x10`

4. Implement the board drawing mechanic, according to these requirements.
    - When drawing the board, the coordinates of fields should also be displayed
(numbers of rows and letters of columns), like this example:
```
  A B C D E
  
1 # # # # #

2 # # # # #

3 # # # # #

4 # # # # #
```
    - During the game, the fields can be either concealed or revealed. The field's letter is displayed only when the field is revealed - when concealed, `#` should be displayed instead.
    - The terminal window is cleaned every time the board is redrawn.

5. Implement the game's logic, to put it all together into a functioning game.
    - The user is welcomed with "Welcome to Memory Game!".
    - The user is asked to select a difficulty level.
    - The letter board is generated, based on the selected difficulty level.
    - The letter board's field are all concealed by default.
    - The board is displayed to the user.
    - The user is asked to select a field, which is then revealed (its letter is being shown on the redrawn board).
    - The user is asked to select another field, which is then revealed (its letter is being shown on the redrawn board).
    - If the two selected fields are a match (have the same letter), they remain revealed for the rest of the game.
    - If the two selected fields aren't a match (don't have the same letters), the user is asked to press Enter. After that, the fields are again concealed.
    - The game ends when all fields are revealed.
    - The game counts how many steps the user made to complete the game and displays this number after winning the game.

## General requirements

None

## Hints

- None

## Background materials

- None
