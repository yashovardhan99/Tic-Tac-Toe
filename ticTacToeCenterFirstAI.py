'''Inheriting from the main ticTacToe game, this is an alternative AI which plays the center move first rather than playing the corners first as in the original AI.
The main goal here is to play this AI against the original AI and see which one wins'''

from ticTacToe import isSpaceFree,getBoardCopy,makeMove,isWinner,chooseRandomMoveFromList
def getAIMove(board,letter):
    #Makes a computer move

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
    
    #Now try for the center
    if isSpaceFree(5,board):
        return 5

    #We try to play the center move as early as possible and only then look for corners

    #Now try for corner moves
    move = chooseRandomMoveFromList(board,[7,9,1,3])
    if move is not None:
        return move
    
    #Other moves on random now
    return chooseRandomMoveFromList(board,[2,4,6,8])