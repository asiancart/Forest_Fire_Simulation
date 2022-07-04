import random , sys

BLANK = ""

def main():
    print("""2048 game by asiancart""")

    input("Press enter to begin")
    gameBoard = getNewBoard()
    while True:
        drawBoard(gameBoard)
        print("Score:",getScore(gameBoard))
        playerMove = askForPlayerMove()
        gameBoard = makeMove(gameBoard,playerMove)
        addTwoToBoard(gameBoard)
        if isFull(gameBoard):
            drawBoard(gameBoard)
            print("Game over - Thanks for playing")
            sys.exit()


def getNewBoard():
    """Returns a new data structure that represents a board.It's a dictionary with keys of (x, y) tuples and values of the tile at that space. The tile is either a power-of-two integer or BLANK.The coordinates are laid out as:
     X0 1 2 3
    Y+-+-+-+-+
    0| | | | |
     +-+-+-+-+
    1| | | | |
     +-+-+-+-+
    2| | | | |
     +-+-+-+-+
    3| | | | |
     +-+-+-+-+"""

    newBoard = {}
    for x in range(4):
        for y in range(4):
            newBoard[(x,y)] = BLANK

    startingTwosPlaced = 0
    while startingTwosPlaced < 2:
        randomSpace = (random.randint(0,3),random.randint(0,3))
        if newBoard[randomSpace] == BLANK:
            newBoard[randomSpace] = 2
            startingTwosPlaced = startingTwosPlaced +1

    return newBoard

def drawBoard(board):
    """Draws the board data structure on the screen."""
    labels = []
    for y in range(4):
        for x in range(4):
            tile = board[(x,y)]
            labelForThisTile = str(tile).center(5)
            labels.append(labelForThisTile)

    print("""
    +-----+-----+-----+-----+
    |     |     |     |     |
    |{}|{}|{}|{}|
    |     |     |     |     |
    +-----+-----+-----+-----+
    |     |     |     |     |
    |{}|{}|{}|{}|
    |     |     |     |     |
    +-----+-----+-----+-----+
    |     |     |     |     |
    |{}|{}|{}|{}|
    |     |     |     |     |
    +-----+-----+-----+-----+
    |     |     |     |     |
    |{}|{}|{}|{}|
    |     |     |     |     |
    +-----+-----+-----+-----+
    """.format(*labels))

def getScore(board):
    """Returns the sum of all the tiles on the board data structure."""
    score = 0
    for x in range(4):
        for y in range(4):
            if board[(x,y)] != BLANK:
                score = score + board[(x,y)]
    return score

def combineTilesInColumn(column):
    """The column is a list of four tile. Index 0 is the "bottom" of the column, and tiles are pulled "down" and combine if they are the same. For example, combineTilesInColumn([2, BLANK, 2, BLANK]) returns [4, BLANK, BLANK, BLANK]."""

    combinedTiles = []
    for i in range(4):
        if column[i] != BLANK:
            combinedTiles.append(column[i])

    while len(combinedTiles) < 4:
        combinedTiles.append(BLANK)

    for i in range(3):
        if combinedTiles[i] == combinedTiles[i+1]:
            combinedTiles[i] *= 2
            for aboveIndex in range(i+1,3):
                combinedTiles[aboveIndex] = combinedTiles[aboveIndex+1]
            combinedTiles[3] = BLANK
    return combinedTiles

def makeMove(board,move):
    """Carries out the move on the board.The move argument is either 'W', 'A', 'S', or 'D' and the function returns the resulting board data structure."""
    if move == "W":
        allColumnsSpaces =  [[(0, 0), (0, 1), (0, 2), (0, 3)],
                             [(1, 0), (1, 1), (1, 2), (1, 3)],
                             [(2, 0), (2, 1), (2, 2), (2, 3)],
                             [(3, 0), (3, 1), (3, 2), (3, 3)]]
    elif move == "A":
        allColumnsSpaces =  [[(0, 0), (1, 0), (2, 0), (3, 0)],
                             [(0, 1), (1, 1), (2, 1), (3, 1)],
                             [(0, 2), (1, 2), (2, 2), (3, 2)],
                             [(0, 3), (1, 3), (2, 3), (3, 3)]]
    elif move == "S":
        allColumnsSpaces =  [[(0, 3), (0, 2), (0, 1), (0, 0)],
                             [(1, 3), (1, 2), (1, 1), (1, 0)],
                             [(2, 3), (2, 2), (2, 1), (2, 0)],
                             [(3, 3), (3, 2), (3, 1), (3, 0)]]
    elif move == "D":
        allColumnsSpaces = [[(3, 0), (2, 0), (1, 0), (0, 0)],
                            [(3, 1), (2, 1), (1, 1), (0, 1)],
                            [(3, 2), (2, 2), (1, 2), (0, 2)],
                            [(3, 3), (2, 3), (1, 3), (0, 3)]]

    boardAfterMove = {}
    for columnSpaces in allColumnsSpaces:
        firstTileSpace = columnSpaces[0]
        secondTileSpace = columnSpaces[1]
        thirdTileSpace = columnSpaces[2]
        fourthTileSpace = columnSpaces[3]

        firstTile = board[firstTileSpace]
        secondTile = board[secondTileSpace]
        thirdTile = board[thirdTileSpace]
        fourthTile = board[fourthTileSpace]

        column = [firstTile,secondTile,thirdTile,fourthTile]
        combinedTilesColumn = combineTilesInColumn(column)

        boardAfterMove[firstTileSpace] = combinedTilesColumn[0]
        boardAfterMove[secondTileSpace] = combinedTilesColumn[1]
        boardAfterMove[thirdTileSpace] = combinedTilesColumn[2]
        boardAfterMove[fourthTileSpace] = combinedTilesColumn[3]

    return boardAfterMove

def askForPlayerMove():
    """Asks the player for the direction of their next move (or quit). Ensures they enter a valid move: either 'W', 'A', 'S' or 'D'."""
    print("Enter move: (WASD or Q to quit)")
    while True:
        move = input("> ").upper()
        if move == "Q":
            print("Thanks for playing")
            sys.exit()
        if move in ("W","A","S","D"):
            return move
        else:
            print('Enter one of "W", "A", "S", "D", or "Q".')


def addTwoToBoard(board):
    """Adds a new 2 tile randomly to the board."""
    while True:
        randomSpace = (random.randint(0,3),random.randint(0,3))
        if board[randomSpace] == BLANK:
            board[randomSpace] = 2
            return

def isFull(board):
    """Returns True if the board data structure has no blanks."""
    for x in range(4):
        for y in range(4):
            if board[(x,y)] == BLANK:
                return False
    return True

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()

