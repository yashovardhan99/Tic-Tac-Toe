'''A TicTacToe demo game - Entirely text based'''

import random

def drawBoard(board):
    #Print the game board as passed
    for i in range(7,10):
        print('|'+board[i],end='|')
    print()
    print('-*--*--*-')
    for i in range(4,7):
        print('|'+board[i],end='|')
    print()
    print('-*--*--*-')
    for i in range(1,4):
        print('|'+board[i],end='|')
    print()

def askPlayerLetters():
    #return the letter chosen by the player along with the AI letter
    print('Choose either X or O:')
    letter = input().upper()
    if letter=='X' or letter=='O':
        print('You have chosen '+letter)
        if letter=='X':
            return ['X','O']
        else:
            return ['O','X']
    else:
        print('Invalid choice - '+letter)
        return askPlayerLetters()

def whoGoesFirst():
    #Randomly decides who goes first
    if random.randint(0,1)==1:
        print("Computer goes first!")
        return 1
    else:
        print("You go first!")
        return 0

def makeMove(letter, board, position):
    #makes changes to the board after a valid move
    board[position]=letter

def isWinner(board,letter):
    #check if the given letter has won in the given board
    return ((board[7]==letter and board[8]==letter and board[9]==letter) or #top
    (board[4]==letter and board[5]==letter and board[6]==letter) or #middle
    (board[1]==letter and board[2]==letter and board[3]==letter) or #bottom
    (board[7]==letter and board[4]==letter and board[1]==letter) or #left
    (board[8]==letter and board[5]==letter and board[2]==letter) or #centre
    (board[9]==letter and board[6]==letter and board[3]==letter) or #right
    (board[7]==letter and board[5]==letter and board[3]==letter) or #left diagonal
    (board[9]==letter and board[5]==letter and board[1]==letter)) #right diagonal

def won(user,letters,moves,board):
    if(user==0):
        print("Congratulations! You("+letters[0]+") won!")
    else:
        print("Oops! the computer("+letters[1]+") won this time. Better luck next time")
    print("The game lasted "+str(moves)+" moves")
    drawBoard(board)

def isSpaceFree(pos,board):
    #Checks if the specified position is free
    return board[pos]==str(pos)

def userMakingMove(board,letter):
    #allows the user to make a valid move
    print("Enter position (1-9) to place "+letter)
    position = int(input())
    if position not in range(1,10):
        print('Invalid position specified')
        userMakingMove(position,board)
    if(not isSpaceFree(position,board)):
        print('That square is already occupied!')
        userMakingMove(board,letter)
    else:
        makeMove(letter,board,position)

#The following functions help the AI make its move
def getBoardCopy(board):
    #Makes a copy of the current board so that the 
    copyBoard = []
    for i in board:
        copyBoard.append(i)
    return copyBoard

def chooseRandomMoveFromList(board,list):
    #returns a random move from all possible moves in the given list
    movesList = []
    for i in list:
        if isSpaceFree(i,board):
            movesList.append(i)
    if len(movesList)==0:
        return None
    else:
        return random.choice(movesList)

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
    
    #Now try for corner moves
    move = chooseRandomMoveFromList(board,[7,9,1,3])
    if move is not None:
        return move
    #Now try for the center
    if isSpaceFree(5,board):
        return 5
    
    #Other moves on random now
    return chooseRandomMoveFromList(board,[2,4,6,8])

def makeAIMove(board,letter):
    AImove = getAIMove(board,letter)
    board[AImove]=letter

gameBoard = [' ']*10
for i in range(1,10):
    gameBoard[i]=str(i)
letters = askPlayerLetters()
current = whoGoesFirst()
gameInProgress = True
moves = 0
while gameInProgress:
    drawBoard(gameBoard)
    if moves>=9:
        print("It's a draw! Well played!")
        gameInProgress = False
        break
    if current==0: #User move
        userMakingMove(gameBoard,letters[0])
        moves = moves+1
        current = 1
        if moves>=5:
            if isWinner(gameBoard,letters[0]):
                won(0,letters,moves,gameBoard)
                gameInProgress=False
                break
    else: #AI move
        print('Computer\'s turn:')
        makeAIMove(gameBoard,letters[1])
        moves = moves+1
        current = 0
        if moves>=5:
            if isWinner(gameBoard,letters[1]):
                won(1,letters,moves,gameBoard)
                gameInProgress=False
                break