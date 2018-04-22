'''I am trying to write a min max algorithm for a tic tac toe AI
Right now the algorithm will continue for about 2 moves. Scoring +10 for each win and -10 for each loss.
Recursion will probably be used
Currently its losing when not starting'''

from ticTacToe import isSpaceFree,getBoardCopy,makeMove,isWinner,chooseRandomMoveFromList

def calculateMoveScore(move,board,letter,factor):
    score = 0
    for i in range(1,10):
        if isSpaceFree(i,board):
            copy = getBoardCopy(board)
            makeMove(letter,copy,i)
            if isWinner(copy,letter):
                score = score + factor*10
            else:
                if letter=='X':
                    opLetter='O'
                else:
                    opLetter='X'
                score = score + calculateMoveScore(i,copy,opLetter,factor*-1)        
    return score

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

    #Starting min max here
    score,move = 0,1 #initial score and move
    for i in range(1,10): #we will try the move which scores the most and choose a random from among them
        if isSpaceFree(i,board):
            copy = getBoardCopy(board)
            makeMove(letter,copy,i)
            s = calculateMoveScore(i,copy,playerLetter,-1)
            if s>score:
                score = s
                move = i
    return move