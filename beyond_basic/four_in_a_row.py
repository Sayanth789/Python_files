'''  
    Four-in-a-Row is a two-player, tile-dropping game. Each player tries to cre-
    ate a row of four of their tiles, whether horizontally, vertically, or diagonally.
    It’s similar to the board games Connect Four and Four Up. The game uses a
    7 by 6 stand-up board, and tiles drop to the lowest unoccupied space in a
    column. In our Four-in-a-Row game, two human players, X and O, will play
    against each other, as opposed to one human player against the computer.

'''

import sys 

# Constants used for displaying the board:
EMPTY_SPACE = "."  #  A period is easier to count than a space 
PLAYER_X = "X"
PLAYER_O = "O"


# Note: Update BOARD_TEMPLATE & COLUMN_LABELS if BOARD_WIDTH is changed.
BOARD_WIDTH = 7 
BOARD_HEIGHT = 6 
COLUMN_LABELS = ("1", "2", "3", "4", "5", "6", "7")
assert len(COLUMN_LABELS) == BOARD_WIDTH


# The Template string for displaying the board:

BOARD_TEMPLATE = """ 

1234567
+-------+
|{}{}{}{}{}{}{}|
|{}{}{}{}{}{}{}|
|{}{}{}{}{}{}{}|
|{}{}{}{}{}{}{}|
|{}{}{}{}{}{}{}|
|{}{}{}{}{}{}{}|
+-------+

"""

def main():
    print("+-------+ 4 in a ROW +-------+")
    print("""Two player take turns dropping tiles into one of seven columns, trying" \
            to make Four-in-a-Row horizontally , vertically, or diagonally.
          """)
    
    # set up a new game

    gameBoard  = getNewBoard()
    playerTurn = PLAYER_X


    while True: # Run a player's turn.
        # Display the board and get player's move:
        displayBoard(gameBoard)
        playerMove = getPlayerMove(playerTurn, gameBoard)
        gameBoard[playerMove] = playerTurn 


        # Check for a win or tie 

        if isWinner(playerTurn, gameBoard):
            displayBoard(gameBoard)   # Display the Board one last time 
            print("Player {} has won!".format(playerTurn))
            sys.exit()
        elif isFull(gameBoard):
            displayBoard(gameBoard)
            print("There is a tie!")
            sys.exit()

        # Switch turns to other player:
        if playerTurn == PLAYER_X:
            playerTurn = PLAYER_O
        elif playerTurn == PLAYER_O:
            playerTurn =PLAYER_X


def getNewBoard():
    """
    Returns a dictionary that represents a Four-in-a-Row board.
        The keys are (columnIndex, rowIndex) tuples of two integers, and the
        values are one of the "X", "O" or "." (empty space) strings.
    """
    board = {}
    for rowIndex in range(BOARD_HEIGHT):
        for columnIndex in range(BOARD_WIDTH):
            board[(columnIndex, rowIndex)] = EMPTY_SPACE 
    return board 


def displayBoard(board):
    """Display the board and its tiles on the screen."""

    # Prepare a list to pass to the format() string method for the board
    # template. The list holds all of the board's tiles (and empty
    # spaces) going left to right, top to bottom:

    tileChars = []
    for rowIndex in range(BOARD_HEIGHT):
        for columnIndex in range(BOARD_WIDTH):
            tileChars.append(board[(columnIndex, rowIndex)])

    # Display the board 
    print(BOARD_TEMPLATE.format(*tileChars))        

def getPlayerMove(playerTile, board):
    """Let a player select a column on the board to drop a tile into."""
    while True:  # keep asking until they enter a valid move 
        print(f"Player {playerTile}, enter 1 to {BOARD_WIDTH} or QUIT:")
        response = input("> ").upper().strip()


        if response == "QUIT":
            print("Thanks for playing!")
            sys.exit()

        if response not in COLUMN_LABELS:
            print(f"Enter a numer from 1 to {BOARD_WIDTH}")
            continue  # Ask player again for their move.

        columnIndex = int(response)  - 1 # -1 as it 0 indexed 

        # if the column is full ask for a move again 
        if board[(columnIndex, 0)] != EMPTY_SPACE:
            print("That column is full, select another one")
            continue

        # Starting from the bottom, find the frist empty space.
        for rowIndex in range(BOARD_HEIGHT - 1, -1, -1):
            if board[(columnIndex, rowIndex)] == EMPTY_SPACE:
                return (columnIndex, rowIndex)
            
def isFull(board):
    """ Return True if the 'board' has no empty spaces, otherwise return False """
    for rowIndex in range(BOARD_HEIGHT):
        for columnIndex in range(BOARD_WIDTH):
            if board[(columnIndex, rowIndex)] == EMPTY_SPACE:
                return False 
            
    return True 
    
def isWinner(playerTile, board):
    """
    Returns True if `playerTile` has four tiles in a row on `board`,
        otherwise returns False.
    """

    #  Go through the entire board, checking for 4 in a row 
    for columnIndex in range(BOARD_WIDTH - 3):
        for rowIndex in range(BOARD_HEIGHT):
            # Check for four-in-a-row going across to the right 
            tile1 = board[(columnIndex, rowIndex)]
            tile2 = board[(columnIndex + 1, rowIndex)]
            tile3 = board[(columnIndex + 2, rowIndex)]
            tile4 = board[(columnIndex + 3, rowIndex)]
            if tile1 == tile2 == tile3 == tile4 == playerTile:
                return True
            
    for columnIndex in range(BOARD_WIDTH):
        for rowIndex in range(BOARD_HEIGHT - 3):
            # Check for four-in-a-row going down:
            tile1 = board[(columnIndex, rowIndex)]
            tile2 = board[(columnIndex, rowIndex + 1)]
            tile3 = board[(columnIndex, rowIndex + 2)]
            tile4 = board[(columnIndex, rowIndex + 3)]
            if tile1 == tile2 == tile3 == tile4 == playerTile:
                return True

    for columnIndex in range(BOARD_WIDTH - 3):
        for rowIndex in range(BOARD_HEIGHT - 3):
            # Check for four-in-a-row going right-down diagonal:            tile1 = board[(columnIndex, rowIndex)]
            tile2 = board[(columnIndex + 1, rowIndex + 1)]
            tile3 = board[(columnIndex + 2, rowIndex + 2)]
            tile4 = board[(columnIndex + 3, rowIndex + 3)]
            if tile1 == tile2 == tile3 == tile4 == playerTile:
                return True
            
    
            # Check for four-in-a-row going left-down diagonal:            tile1 = board[(columnIndex + 3, rowIndex)]
            tile2 = board[(columnIndex + 2, rowIndex + 1)]
            tile3 = board[(columnIndex + 1, rowIndex + 2)]
            tile4 = board[(columnIndex, rowIndex + 3)]
            if tile1 == tile2 == tile3 == tile4 == playerTile:
                return True

    return False 

if __name__ == "__main__":
    main() 

                    






            






    