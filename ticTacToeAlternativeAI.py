'''From trials, this AI also considers the opponent's moves before placing its own move. This AI has not yet been defeated when it starts first!'''
from ticTacToe import isSpaceFree,getBoardCopy,makeMove,isWinner,chooseRandomMoveFromList

def returnOppositeCorner(corner):
    #returns opposite corner for the game board
    if corner==7:
        return 3
    elif corner==9:
        return 1
    elif corner==1:
        return 9
    else:
        return 7

def getAIMove(board,letter):
    #Makes a single AI move

    #firstly check if a win is possible
    for i in range(1,10):
        if isSpaceFree(i,board):
            copy = getBoardCopy(board)
            makeMove(letter,copy,i)#test if a win is possible by making a demo move in a copy board
            if(isWinner(copy,letter)):
                return i
    #Now check if user is winning and try to block that
    if letter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X' #First find the player letter
    for i in range(1,10):
        if isSpaceFree(i,board):
            copy = getBoardCopy(board)
            makeMove(playerLetter,copy,i)
            if(isWinner(copy,playerLetter)):
                return i
    #Now it will check if a corner opposite to its piece is free and play it
    for i in [1,3,7,9]:
        if board[i]==letter: #occupied by it's own piece
            if isSpaceFree(returnOppositeCorner(i),board):
                return returnOppositeCorner(i)

    #Now try for the center
    if isSpaceFree(5,board):
        return 5

    #Now try for random corners where opposite corners are not blocked
    for i in [1,3,7,9]:
        if isSpaceFree(i,board) and isSpaceFree(returnOppositeCorner(i),board):
            return i
    
    
    #Other moves on random now
    move = chooseRandomMoveFromList(board,[2,4,6,8])
    if move is None:
        return chooseRandomMoveFromList(board,[1,3,7,9])# if only a corner is free
    else:
        return move
