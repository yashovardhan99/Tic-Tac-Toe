'''Used to start a human vs AI match in ticTacToe'''
from ticTacToe import askPlayerLetters,whoGoesFirst,drawBoard,userMakingMove,isWinner,won,makeAIMove
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