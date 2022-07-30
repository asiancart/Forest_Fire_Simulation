import random , sys

try:
    import bext
except ImportError:
    print('This program requires the bext module')
    sys.exit()


BOARD_WIDTH = 16
BOARD_HEIGHT = 14
MOVES_PER_GAME = 20

HEART = chr(9829)
DIAMOND = chr(9830)
SPADE = chr(9824)
CLUB = chr(9827)
BALL = chr(9679)
TRIANGLE = chr(9650)

BLOCK = chr(9608)
LEFTRIGHT = chr(9472)
UPDOWN = chr(9474)
DOWNRIGHT = chr(9484)
DOWNLEFT = chr(9488)
UPRIGHT = chr(9492)
UPLEFT = chr(9496)

TILE_TYPES = (0,1,2,3,4,5)
COLORS_MAP ={0: "red", 1: "green", 2: "blue", 3: "yellow", 4: "cyan", 5: "purple"}
COLOR_MODE = "color mode"
SHAPES_MAP = {0: HEART, 1: TRIANGLE, 2: DIAMOND,3: BALL, 4: CLUB, 5: SPADE}
SHAPE_MODE = "shape mode"

def main():
    bext.bg("black")
    bext.fg("white")
    bext.clear()
    print("""flooder by asiancart""")
    print('Do you want to play in colorblind mode? Y/N')
    response = input('> ')
    if response.upper().startswith("Y"):
        displayMode = SHAPE_MODE
    else:
        displayMode = COLOR_MODE

    gameBoard = getNewBoard()
    movesLeft = MOVES_PER_GAME

    while True:
        displayBoard(gameBoard,displayMode)

        print("Moves left: ",movesLeft)
        playerMove = askForPlayerMove(displayMode)
        changeTile(playerMove,gameBoard,0,0)
        movesLeft -=1

        if hasWon(gameBoard):
            displayBoard(gameBoard,displayMode)
            print("You have won")
            break
        elif movesLeft == 0:
            displayBoard(gameBoard,displayMode)
            print("You have run out of moves!")
            break

def getNewBoard():
    board = {}

    for x in range(BOARD_WIDTH):
        for y in range(BOARD_HEIGHT):
            board[(x,y)] = random.choice(TILE_TYPES)

    for i in range(BOARD_WIDTH*BOARD_HEIGHT):
        x = random.randint(0,BOARD_WIDTH-2)
        y = random.randint(0,BOARD_HEIGHT-1)
        board[(x+1,y)] = board[(x,y)]
    return board

def displayBoard(board,displayMode):
    bext.fg("white")
    print(DOWNRIGHT+(LEFTRIGHT*BOARD_WIDTH)+ DOWNLEFT)

    for y in range(BOARD_HEIGHT):
        bext.fg("white")
        if y == 0:
            print(">", end="")
        else:
            print(UPDOWN,end="")

        for x in range(BOARD_WIDTH):
            bext.fg(COLORS_MAP[board[(x,y)]])
            if displayMode == COLOR_MODE:
                print(BLOCK, end='')
            elif displayMode == SHAPE_MODE:
                print(SHAPE_MAP[board[(x,y)]],end="")

        bext.fg("white")
        print(UPDOWN)
    print(UPRIGHT+ (LEFTRIGHT*BOARD_WIDTH)+ UPLEFT)

def askForPlayerMove(displayMode):
    while True:
        bext.fg("white")
        print("Chose one of ", end="")

        if displayMode== COLOR_MODE:
            bext.fg("red")
            print('(R)ed ', end='')
            bext.fg("green")
            print('(G)reen ', end='')
            bext.fg("blue")
            print('(B)lue ', end='')
            bext.fg("yellow")
            print('(Y)ellow ', end='')
            bext.fg("cyan")
            print('(C)yan ', end='')
            bext.fg("purple")
            print('(P)urple ', end='')
        else:
            bext.fg("red")
            print('(H)eart, ', end='')
            bext.fg("green")
            print('(T)riangle, ', end='')
            bext.fg("blue")
            print('(D)iamond, ', end='')
            bext.fg("yellow")
            print('(B)all, ', end='')
            bext.fg("cyan")
            print('(C)lub, ', end='')
            bext.fg("purple")
            print('(S)pade, ', end='')
        bext.fg("white")
        print('or QUIT:')
        response = input("> ").upper()
        if response == "QUIT":
            print("Thanks for playing!")
            sys.exit()
        if displayMode == COLOR_MODE:
            return {'R': 0, 'G': 1, 'B': 2,'Y': 3, 'C': 4, 'P': 5}[response]
        if displayMode == SHAPE_MODE and response in tuple('HTDBCS'):
            return {'H': 0, 'T': 1, 'D': 2,'B': 3, 'C': 4, 'S': 5}[response]

def changeTile(tileType,board,x,y,charToChange=None):
    if x == 0 and y == 0:
        charToChange = board[(x,y)]
        if tileType == charToChange:
            return

    board[(x,y)]=tileType

    if x > 0 and board[(x - 1, y)] == charToChange:
        changeTile(tileType, board, x - 1, y, charToChange)
    if y > 0 and board[(x, y - 1)] == charToChange:
        changeTile(tileType, board, x, y - 1, charToChange)
    if x < BOARD_WIDTH - 1 and board[(x + 1, y)] == charToChange:
        changeTile(tileType, board, x + 1, y, charToChange)
    if y < BOARD_HEIGHT - 1 and board[(x, y + 1)] == charToChange:
        changeTile(tileType, board, x, y + 1, charToChange)

def hasWon(board):
    tile = board[(0,0)]

    for x in range(BOARD_WIDTH):
        for y in range(BOARD_HEIGHT):
            if board[(x,y)] != tile:
                return False
    return True

if __name__ == "__main__":
    main()



