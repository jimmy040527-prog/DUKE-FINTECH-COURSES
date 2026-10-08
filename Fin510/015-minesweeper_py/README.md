# Minesweeper

For this problem, you complete a partially written minesweeper game. 
This game will be played on a text interface (not a GUI---we have not
learned anything about those).

If you are not familiar with the game of minesweeper, you might take a minute to read up about it on the internet (https://en.wikipedia.org/wiki/Minesweeper_(video_game), but you don't need much game expertise to do this assignment.

We have provided code for an almost working minesweeper, except the code has been removed for four functions:
```python
make_board(width, height, nun_mines)
count_mines(board, int x, int y)
check_win(board )
reveal_mines(board)
```

Each of the functions has a docstring describing the necessary behavior.

The board must be represented as a list of lists.  We will follow the normal
convention with programs where the first list (the outer) contains the rows.
So each element in that list is also a list. Each element in the inner list
is an integer.  As you'll see in minesweeper.py, we have defined several
variables at the top of the file to serve as "constants" for the program.
"Constants" is in quotes as Python does not have this concept (most other
programming do) - Python relies upon programmers being good citizens and not
changing items that they should not.  

That integer in the "list of lists" is a negative based on the following conditions:
```python
SQUARE_UNKNOWN     = -1   # The square does not contain a mine, but the user does not know that
SQUARE_HAS_MINE    = -2   # We have assigned a mine to the square, but the user does not know that
SQUARE_KNOWN_MINE  = -3   # The user has determined that the square contains a mine
```
if the `square >= 0`, that represents the number of mines surrounding the square.

When we index the board, it will be done in this fashion:
   `board[y][x]`
or 
   `board[row][col]`

- `make_board` should first create and initialize each element of the board
   to SQUARE_UNKNOWN.  Then the function must call `add_random_mine` an
   appropriate number of times (i.e., `numMines`) to "randomly" place mines
   on the board.

   We explicitly set a seed for random in the "main" routine of the code.
   This causes the same "random" board to be generated.

 - `count_mines`: this function takes a board and an (x,y) coordinate.
    It should count the mines in the 8 squares around that (x,y) 
    coordinate, and return that count.  Note that a mine may be
    indicated by a square on the board either being HAS_MINE or
    KNOWN_MINE.  You can use the has_mine function to test both cases:
    ```python
    has_mine(board[ny][nx])
    ```     
    (given the previously created board and (nx,ny) are the coordinates you
    want to check).  Be careful not to go out of bounds of the list.

 - `check_win`: this function takes a board and sees if the game has
    been won.  The game is won when no squares are UNKNOWN.
 - `reveal_mines`: this function takes a board and converts all
    entries that have "SQUARE_HAS_MINE" to "SQUARE_KNOWN_MINE".
    This function is called when a player loses. We want the player
    to see the location of all of the hidden mines. 

Notes: 
- You should NOT change any of the other provided functions!
- Pay careful attention to the indexes and their order.

Once you have these all working, you should have a playable game of 
minesweeper.  Note that there are a few differences in gameplay
from the "standard" game:
 - You select a square by entering its x (column) and y (row) coordinates.
   The x coordinates are listed across the top and the y are listed
   down the left side to reduce counting.
 - The game will automatically figure out the "obvious" squares:
   both mines and non-mined spaces.  It will reveal these to you 
   as soon as it considers them trivial to figure out.  
 - You cannot manually mark a square that you suspect has a mine


To assist with both development and testing, you may want to create a
`test_minesweeper.py` file.  You can then place Python statements in that
file to make function calls to those within minesweeper.py.  Earlier
assignments have utilized this pattern.

## Example test_minesweeper.py
```python
import minesweeper
import random 

random.seed(42)   # do this for repeatability

board = minesweeper.make_board(4,5,10)
print(board)
minesweeper.print_board(board)
print(minesweeper.board_height(board))
print(minesweeper.board_width(board))
# add additional checks ...
```

## Example output for that code:
```text
[[-2, -1, -2, -2], [-1, -2, -2, -2], [-1, -1, -1, -1], [-1, -2, -1, -1], [-2, -2, -1, -2]]
   0000
   0123
-------
 0|????
 1|????
 2|????
 3|????
 4|????
5
4
``` 

Once your code is complete, submit `minesweeper.py`.